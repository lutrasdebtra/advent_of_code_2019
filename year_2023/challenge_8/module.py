from typing import List
import networkx as nx
import re
import math


class Direction:
    def __init__(self, directions: str):
        self.directions = list(directions)
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        direction = self.directions[self.idx]

        if self.idx + 1 > (len(self.directions) - 1):
            self.idx = 0
        else:
            self.idx += 1
        return direction


def _create_graph(graph: List[str]) -> nx.DiGraph:
    G = nx.DiGraph()
    for nodes in graph[2:]:
        parent_node, left_node, right_node = re.findall(r"[A-Z1-9]+", nodes)
        if left_node == right_node:
            G.add_edge(parent_node, left_node, direction="LR")
        else:
            G.add_edge(parent_node, left_node, direction="L")
            G.add_edge(parent_node, right_node, direction="R")
    return G


def _next_edge(G: nx.DiGraph, direction: str, current_node: str) -> str:
    for edge, attr in G[current_node].items():
        if direction in attr["direction"]:
            return edge


def calculate_path_length(graph: List[str]) -> int:
    directions = Direction(directions=graph[0])
    G = _create_graph(graph=graph)

    current_node = "AAA"
    steps = 0
    for direction in directions:
        if current_node == "ZZZ":
            return steps
        current_node = _next_edge(G=G, direction=direction, current_node=current_node)
        steps += 1


def calculate_simultaneous_path_length(graph: List[str]) -> int:
    G = _create_graph(graph=graph)

    current_nodes = [node for node in list(G.nodes) if node.endswith("A")]

    lcms = []
    for node in current_nodes:
        current_node = node
        steps = 0
        for direction in Direction(directions=graph[0]):
            if current_node.endswith("Z"):
                lcms.append(steps)
                break
            current_node = _next_edge(
                G=G, direction=direction, current_node=current_node
            )
            steps += 1
    return math.lcm(*lcms)
