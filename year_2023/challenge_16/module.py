from typing import List, Set, Tuple
from collections import deque

COMPASS_OPPS = {
    "N": "S",
    "S": "N",
    "E": "W",
    "W": "E",
}

SYMBOL_NEXT_DIRECTION = {
    (".", "N"): ["S"],
    (".", "S"): ["N"],
    (".", "E"): ["W"],
    (".", "W"): ["E"],
    ("/", "N"): ["W"],
    ("/", "S"): ["E"],
    ("/", "E"): ["S"],
    ("/", "W"): ["N"],
    ("\\", "N"): ["E"],
    ("\\", "S"): ["W"],
    ("\\", "E"): ["N"],
    ("\\", "W"): ["S"],
    ("-", "N"): ["W", "E"],
    ("-", "S"): ["W", "E"],
    ("-", "E"): ["W"],
    ("-", "W"): ["E"],
    ("|", "N"): ["S"],
    ("|", "S"): ["N"],
    ("|", "E"): ["N", "S"],
    ("|", "W"): ["N", "S"],
}

COMPASS_POSITIONS = {
    "N": lambda x, y: (x - 1, y),
    "S": lambda x, y: (x + 1, y),
    "E": lambda x, y: (x, y + 1),
    "W": lambda x, y: (x, y - 1),
}


def _print_mirror(mirrors: List[List[str]], energised_set: Set[Tuple[int, int]]):
    print()
    for x in range(len(mirrors)):
        l = ""
        for y in range(len(mirrors[x])):
            l += "#" if (x, y) in energised_set else mirrors[x][y]
        print(l)


def calculate_energy(
    mirrors: List[str], starting_point: Tuple[int, int, str] = (0, 0, "W")
) -> int:
    mirrors = [list(m) for m in mirrors]
    beams = deque([starting_point])
    energised_set = {(starting_point[0], starting_point[1])}
    energised_set_edges = set()
    cycle = 1
    while len(beams) > 0:
        cycle += 1
        x, y, direction = beams.popleft()
        if (x < 0 or x >= len(mirrors)) or (y < 0 or y >= len(mirrors[0])):
            continue
        energised_set.add((x, y))
        current_symbol = mirrors[x][y]
        next_directions = SYMBOL_NEXT_DIRECTION[(current_symbol, direction)]
        for nxt_dir in next_directions:
            new_x, new_y = COMPASS_POSITIONS[nxt_dir](x, y)
            if (x, y, new_x, new_y) in energised_set_edges:
                continue
            energised_set_edges.add((x, y, new_x, new_y))
            beams.append((new_x, new_y, COMPASS_OPPS[nxt_dir]))
    return len(energised_set)


def calculate_maximum_possible_energy(mirrors: List[str]) -> int:
    north_coords = [(0, y, "N") for y in range(len(mirrors[0]))]
    south_coords = [((len(mirrors) - 1), y, "S") for y in range(len(mirrors[0]))]
    west_coords = [(x, 0, "W") for x in range(len(mirrors))]
    east_coords = [(x, (len(mirrors) - 1), "E") for x in range(len(mirrors))]

    coords = north_coords + south_coords + west_coords + east_coords
    coord_len = len(coords)
    energies = []
    for idx, coord in enumerate(coords):
        print(f"{idx+1}/{coord_len}")
        energies.append(calculate_energy(mirrors=mirrors.copy(), starting_point=coord))
    return max(energies)
