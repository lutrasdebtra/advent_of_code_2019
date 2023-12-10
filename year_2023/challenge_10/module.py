from typing import List, Tuple, Optional
from matplotlib.path import Path

SYMBOLS = ["|", "-", "L", "J", "7", "F"]

SYMBOL_DIRECTIONS = {
    "|": ["N", "S"],
    "-": ["E", "W"],
    "L": ["N", "E"],
    "J": ["N", "W"],
    "7": ["S", "W"],
    "F": ["S", "E"],
}

SYMBOL_DIRECTIONS_REVERSED = {tuple(sorted(v)): k for k, v in SYMBOL_DIRECTIONS.items()}

SYMBOL_NEXT_DIRECTION = {
    ("|", "N"): "S",
    ("|", "S"): "N",
    ("-", "E"): "W",
    ("-", "W"): "E",
    ("L", "N"): "E",
    ("L", "E"): "N",
    ("J", "N"): "W",
    ("J", "W"): "N",
    ("7", "S"): "W",
    ("7", "W"): "S",
    ("F", "S"): "E",
    ("F", "E"): "S",
}

COMPASS_OPPS = {
    "N": "S",
    "S": "N",
    "E": "W",
    "W": "E",
}

COMPASS_POSITIONS = {
    "N": lambda x, y: (x - 1, y),
    "S": lambda x, y: (x + 1, y),
    "E": lambda x, y: (x, y + 1),
    "W": lambda x, y: (x, y - 1),
}


def _get_start_pos(pipes: List[str]) -> Tuple[int, int]:
    for x in range(len(pipes)):
        for y in range(len(pipes[x])):
            if pipes[x][y] == "S":
                return x, y


def _get_symbol(pipes: List[str], x: int, y: int) -> Optional[str]:
    try:
        return pipes[x][y] if pipes[x][y] != "." else None
    except IndexError:
        return None


def _determine_start_symbol(pipes: List[str], x: int, y: int) -> str:
    """
    Checks all neighbouring symbols and then determines if the neighbour can go in the opposite direction.
    """
    surrounding_directions = []
    for direction in ["N", "S", "E", "W"]:
        neighbour_x, neighbour_y = COMPASS_POSITIONS[direction](x, y)
        neighbour_symbol = _get_symbol(pipes=pipes, x=neighbour_x, y=neighbour_y)
        if neighbour_symbol:
            if (neighbour_symbol, COMPASS_OPPS[direction]) in SYMBOL_NEXT_DIRECTION:
                surrounding_directions.append(direction)
    return SYMBOL_DIRECTIONS_REVERSED[tuple(sorted(surrounding_directions))]


def _generate_cycle_coords(pipes: List[str]) -> List[Tuple[int, int]]:
    x, y = _get_start_pos(pipes=pipes)
    cycle = [(x, y)]
    symbol = _determine_start_symbol(pipes=pipes, x=x, y=y)
    direction = SYMBOL_DIRECTIONS[symbol][0]
    while True:
        x, y = COMPASS_POSITIONS[direction](x, y)
        symbol = _get_symbol(pipes=pipes, x=x, y=y)
        if symbol == "S":
            break
        direction = SYMBOL_NEXT_DIRECTION[(symbol, COMPASS_OPPS[direction])]
        cycle.append((x, y))
    return cycle


def calculate_farthest_point(pipes: List[str]) -> int:
    cycle = _generate_cycle_coords(pipes=pipes)
    return len(cycle) // 2


def calculate_cycle_cover(pipes: List[str]) -> int:
    """
    Solution from https://old.reddit.com/r/adventofcode/comments/18evyu9/2023_day_10_solutions/kcqgqet/
    See: https://matplotlib.org/stable/api/path_api.html
    """
    cycle = _generate_cycle_coords(pipes=pipes)
    internal_tiles = 0
    p = Path(cycle)
    for x in range(len(pipes)):
        for y in range(len(pipes[x])):
            if (x, y) in cycle:
                continue
            if p.contains_point((x, y)):
                internal_tiles += 1
    return internal_tiles
