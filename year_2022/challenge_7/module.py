from typing import List, Text
import networkx as nx


def _generate_directory_structure(commands: List[Text]) -> nx.DiGraph:
    G = nx.DiGraph()
    current_directory = None
    for command in commands:
        # Input.
        if command.startswith("$"):
            if command.startswith("$ cd"):
                cd_param = command.split()[-1]
                # Go to previous directory.
                if cd_param == "..":
                    parent = list(G.predecessors(current_directory))
                    if parent:
                        current_directory = parent[0]
                # Access directory
                else:
                    current_directory = cd_param
                    if not G.has_node(current_directory):
                        G.add_node(current_directory)
        # Output.
        else:
            command_1, command_2 = command.split()
            G.add_node(command_2)
            G.add_edge(current_directory, command_2)
            if command_1.isdigit():
                G.nodes[command_2]["size"] = int(command_1)

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
        print(node, size)
        if size <= 100000:
            total_size += size
    return total_size
