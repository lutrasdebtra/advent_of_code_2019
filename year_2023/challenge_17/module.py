from typing import List
from heapq import heappop, heappush
from math import inf

NEW_DIRECTION_COORDS = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
)

REVERSE_CHECK = {0: 1, 1: 0, 2: 3, 3: 2}


def calculate_shortest_distance(city_blocks: List[str], ultra: bool = False) -> int:
    city_blocks = [[int(x) for x in c] for c in city_blocks]
    len_x = len(city_blocks)
    len_y = len(city_blocks[0])
    source_x, source_y, target_x, target_y = (
        0,
        0,
        (len(city_blocks) - 1),
        (len(city_blocks[0]) - 1),
    )
    queue = [(0, source_x, source_y, -1, -1)]
    distances = {}
    min_heat_loss = inf

    if ultra:
        min_moves, max_moves = 4, 10
    else:
        min_moves, max_moves = 0, 3

    while queue:
        distance, x, y, direction, direction_count = heappop(queue)
        if (x, y, direction, direction_count) in distances:
            continue
        distances[(x, y, direction, direction_count)] = distance
        if x == target_x and y == target_y and direction_count >= min_moves:
            min_heat_loss = min(min_heat_loss, distance)
        for i, (dx, dy) in enumerate(NEW_DIRECTION_COORDS):
            new_x = x + dx
            new_y = y + dy

            if not (0 <= new_x < len_x and 0 <= new_y < len_y):
                continue

            new_direction = i
            new_direction_count = (
                1 if new_direction != direction else direction_count + 1
            )

            # Base case for first entry in queue.
            if direction_count != -1:
                if REVERSE_CHECK[new_direction] == direction:
                    continue

                if new_direction_count > max_moves:
                    continue

                if direction != new_direction and direction_count < min_moves:
                    continue

            heappush(
                queue,
                (
                    distance + city_blocks[new_x][new_y],
                    new_x,
                    new_y,
                    new_direction,
                    new_direction_count,
                ),
            )
    return min_heat_loss
