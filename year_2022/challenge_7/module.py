from typing import List, Text
import networkx as nx


def _generate_directory_structure(commands: List[Text]) -> nx.DiGraph:
    G = nx.DiGraph()
    current_directory = ""
    for command in commands:
        # Input.
        if command.startswith("$"):
            if command.startswith("$ cd"):
                cd_param = command.split()[-1]
                # Go to previous directory.
                if cd_param == "..":
                    current_directory = "-".join(current_directory.split("-")[:-1])
                # Access directory
                else:
                    if current_directory:
                        current_directory = f"{current_directory}-{cd_param}"
                    else:
                        current_directory = cd_param
                    if not G.has_node(current_directory):
                        G.add_node(current_directory)
        # Output.
        else:
            command_1, command_2 = command.split()
            node_name = f"{current_directory}-{command_2}"
            G.add_node(node_name)
            G.add_edge(current_directory, node_name)
            if command_1.isdigit():
                G.nodes[node_name]["size"] = int(command_1)

    # Add size attributes to directory (non-leaf) nodes.
    for node in list(nx.bfs_tree(G, "/")):
        if not G.nodes[node].get("size"):
            G.nodes[node]["size"] = sum(
                int(G.nodes[d].get("size", 0)) for d in nx.descendants(G, node)
            )
    return G


def directory_size(commands: List[Text]) -> int:
    G = _generate_directory_structure(commands)
    total_size = 0
    for node in [x for x in G.nodes() if G.out_degree(x) > 0]:
        size = G.nodes[node]["size"]
        if size <= 100000:
            total_size += size
    return total_size


def directory_to_delete(commands: List[Text]) -> int:
    G = _generate_directory_structure(commands)
    unused_space = 70000000 - G.nodes["/"]["size"]
    space_to_free = 70000000
    node_to_delete = None
    for node in [x for x in G.nodes() if G.out_degree(x) > 0]:
        size = G.nodes[node]["size"]
        tmp = size + unused_space
        if 30000000 < tmp < space_to_free:
            space_to_free = tmp
            node_to_delete = node
    return G.nodes[node_to_delete]["size"]
