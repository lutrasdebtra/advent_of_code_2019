from typing import List, Tuple
import networkx as nx

COMPASS_POSITIONS = {
    "N": lambda x, y: (x - 1, y),
    "S": lambda x, y: (x + 1, y),
    "E": lambda x, y: (x, y + 1),
    "W": lambda x, y: (x, y - 1),
}

COMPASS_ROCK_ORDER = {
    "N": lambda rocks_x, rocks_y, G: (
        (x, y)
        for x in range(rocks_x)
        for y in range(rocks_y)
        if (x, y) in G and G.nodes[(x, y)].get("movable", False)
    ),
    "S": lambda rocks_x, rocks_y, G: (
        (x, y)
        for x in reversed(range(rocks_x))
        for y in reversed(range(rocks_y))
        if (x, y) in G and G.nodes[(x, y)].get("movable", False)
    ),
    "E": lambda rocks_x, rocks_y, G: (
        (x, y)
        for y in reversed(range(rocks_y))
        for x in reversed(range(rocks_x))
        if (x, y) in G and G.nodes[(x, y)].get("movable", False)
    ),
    "W": lambda rocks_x, rocks_y, G: (
        (x, y)
        for y in range(rocks_y)
        for x in range(rocks_x)
        if (x, y) in G and G.nodes[(x, y)].get("movable", False)
    ),
}


def _get_movable_rocks(G: nx.Graph) -> Tuple[Tuple[int, int], ...]:
    return tuple(
        node for node, data in G.nodes(data=True) if data.get("movable", False)
    )


def calculate_load(
    rocks: List[str], cycles: int = 1, cycle_directions: str = "N"
) -> int:
    rocks = [list(x) for x in rocks]
    rocks_x, rocks_y = len(rocks), len(rocks[0])

    G = nx.grid_2d_graph(len(rocks), len(rocks[0]))

    for x in range(rocks_x):
        for y in range(rocks_y):
            if rocks[x][y] == "#":
                G.remove_node((x, y))
            elif rocks[x][y] == "O":
                G.nodes[(x, y)]["movable"] = True

    seen_cycles = {0: _get_movable_rocks(G=G)}
    cycle_pattern = seen_cycles[0]

    cycle_num = 0
    while cycle_num < cycles:
        cycle_num += 1
        for direction in cycle_directions:
            move_func = COMPASS_POSITIONS[direction]
            for rock in COMPASS_ROCK_ORDER[direction](rocks_x, rocks_y, G):
                new_pos = rock
                while True:
                    tmp = move_func(new_pos[0], new_pos[1])
                    if tmp not in G or G.nodes[tmp].get("movable", False):
                        break
                    new_pos = tmp
                G.nodes[rock]["movable"] = False
                G.nodes[new_pos]["movable"] = True

        cycle_pattern = _get_movable_rocks(G=G)
        if cycle_pattern in seen_cycles:
            # Work out how often the cycle repeats
            last = seen_cycles[cycle_pattern]
            cycle_repeats = cycle_num - last
            # The difference between the repeat and the final answer is the remainder of the repeats from the
            # Remaining cycles.
            cycle_remainder = (cycles - cycle_num) % cycle_repeats
            # The solution is then just the last time we saw the current cycle + the remainder.
            final_idx = last + cycle_remainder
            # Dict keys are ordered in 3.7+.
            cycle_pattern = list(seen_cycles.keys())[final_idx]
            break
        else:
            seen_cycles[cycle_pattern] = cycle_num

    load = 0
    for x, y in cycle_pattern:
        load += len(rocks) - x
    return load
