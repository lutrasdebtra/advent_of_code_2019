from typing import List
from shapely.geometry import Polygon, Point
from collections import deque

DIRECTION_MOVES = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}

DIRECTION_CODES = {0: "R", 1: "D", 2: "L", 3: "U"}


def calculate_area(directions: List[str], use_hex_instructions: bool = False) -> int:
    processed_directions = []
    for line in directions:
        direction, distance, colour = line.split(" ")
        if use_hex_instructions:
            h = colour[2:-1]
            distance, direction = int(h[:5], 16), DIRECTION_CODES[int(h[-1], 16)]
            processed_directions.append((direction, distance, colour[1:-1]))
        else:
            processed_directions.append((direction, int(distance), colour[1:-1]))

    borders = []
    x, y, perimeter = 0, 0, 0
    for direction, distance, _ in processed_directions:
        dx, dy = DIRECTION_MOVES[direction]
        borders.append((x, y))
        perimeter += distance
        x += dx * distance
        y += dy * distance

    # Polygon only needs turn coords to build a complete shape
    # This skips using Shoelace theorem directly.
    poly = Polygon(borders)

    # Pick's theorem: https://en.wikipedia.org/wiki/Pick%27s_theorem
    interior_area = poly.area - perimeter // 2 + 1
    return int(interior_area + perimeter)
