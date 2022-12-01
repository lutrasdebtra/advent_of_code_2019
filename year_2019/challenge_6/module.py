import networkx as nx


def _create_graph(path, directed=True):
    g = nx.read_edgelist(
        path, delimiter=")", create_using=(nx.DiGraph if directed else nx.Graph)
    )
    if directed:
        return g.reverse()
    return g


def count_simple_paths(path):
    graph = _create_graph(path)
    paths_count = 0
    for n in graph.nodes():
        paths = list(nx.all_simple_paths(graph, source=n, target="COM"))
        for path in paths:
            # Count edges not nodes.
            paths_count += len(path) - 1
    return paths_count


def shortest_path(path, source="YOU", dest="SAN"):
    graph = _create_graph(path, directed=False)
    orbit_1 = list(nx.neighbors(graph, source))[0]
    orbit_2 = list(nx.neighbors(graph, dest))[0]
    # Count edges not nodes.
    return len(nx.shortest_path(graph, source=orbit_1, target=orbit_2)) - 1
