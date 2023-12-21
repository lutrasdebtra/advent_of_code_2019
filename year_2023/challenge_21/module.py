from typing import List
import networkx as nx

NEW_DIRECTION_COORDS = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
)


def calculate_reachable_plots(garden_plots: List[str], cutoff: int = 6) -> int:
    garden_plots_x, garden_plots_y = len(garden_plots), len(garden_plots[0])
    G = nx.grid_2d_graph(garden_plots_x, garden_plots_y)

    source = None

    for x in range(garden_plots_x):
        for y in range(garden_plots_y):
            if garden_plots[x][y] == "#":
                G.remove_node((x, y))
            elif garden_plots[x][y] == "S":
                source = (x, y)

    plots_at_cutoff = set()
    visited = set()
    queue = [(source[0], source[1], 0)]
    while queue:
        x, y, dist = queue.pop(0)
        if (x, y, dist) in visited:
            continue
        visited.add((x, y, dist))
        if dist == cutoff:
            plots_at_cutoff.add((x, y))
        dist += 1
        for dx, dy in NEW_DIRECTION_COORDS:
            new_x, new_y = x + dx, y + dy
            if (
                (0 <= new_x < garden_plots_x)
                and (0 <= new_y < garden_plots_y)
                and garden_plots[new_x][new_y] != "#"
                and (dist <= cutoff)
            ):
                queue.append((new_x, new_y, dist))
    return len(plots_at_cutoff)
