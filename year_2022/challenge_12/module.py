from typing import List, Text, Optional
import networkx as nx


def _calculate_edge_validity(node_1: str, node_2: str):
    node_map = {"S": "a", "E": "z"}
    return ord(node_map.get(node_2, node_2)) <= ord(node_map.get(node_1, node_1)) + 1


def _node_name(x: int, y: int, l: str) -> str:
    return l if l.isupper() else f"{l}-({x},{y})"


def hill_climb(elevations: List[List[Text]], source: Optional[Text] = "S") -> int:
    G = nx.DiGraph()
    for x in range(len(elevations)):
        for y in range(len(elevations[x])):
            for x_1, y_1 in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                try:
                    if _calculate_edge_validity(elevations[x][y], elevations[x_1][y_1]):
                        G.add_edge(
                            _node_name(x, y, elevations[x][y]),
                            _node_name(x_1, y_1, elevations[x_1][y_1]),
                        )
                except IndexError:
                    continue
    p = nx.shortest_path_length(G, target="E")
    return min(p[k] for k in p.keys() if k[0] == source)
