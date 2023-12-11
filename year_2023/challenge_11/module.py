from typing import List
import networkx as nx
import numpy as np
from itertools import combinations


def calculate_shortest_path_lengths(universe: List[str], expansion: int = 2) -> int:
    np_universe = np.array([list(x) for x in universe])
    rows_to_expand, columns_to_expand = [], []

    for idx, row in enumerate(np_universe):
        if "#" not in row:
            rows_to_expand.append(idx)

    # Transpose the array to check the columns.
    for idx, column in enumerate(np_universe.T):
        if "#" not in column:
            columns_to_expand.append(idx)

    galaxy_coords = list(zip(*np.where(np_universe == "#")))

    G = nx.grid_2d_graph(np_universe.shape[0], np_universe.shape[1])
    nx.set_edge_attributes(G, 1, name="weight")

    # Add the expansion weight to the incoming edge.
    for x in rows_to_expand:
        for y in range(np_universe.shape[1]):
            G[(x - 1, y)][(x, y)]["weight"] = expansion

    for y in columns_to_expand:
        for x in range(np_universe.shape[0]):
            G[(x, y - 1)][(x, y)]["weight"] = expansion

    shortest_path_lengths = 0

    for start, end in combinations(galaxy_coords, 2):
        shortest_path_lengths += nx.path_weight(
            G, nx.shortest_path(G, start, end), weight="weight"
        )
    return shortest_path_lengths
