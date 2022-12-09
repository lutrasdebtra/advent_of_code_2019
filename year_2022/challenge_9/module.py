from typing import List, Tuple, Text, Optional
from collections import deque


def make_grid(items):
    return [[" " for _ in range(0, 100)] for _ in range(0, 100)]


def place_on_grid(grid, x, y, c="#"):
    grid[x][y] = c


def repr_grid(grid):
    return "\n".join("|" + "|".join(sub + [""]) for sub in grid)


def place_items_on_grid(data, head):
    grid = make_grid(data)
    for x, y in data:
        place_on_grid(grid, x, y)
        place_on_grid(grid, 50, 50, c="S")
        place_on_grid(grid, head[0], head[1], c="H")
    print(repr_grid(grid))


####


def _move(direction: Text, pos: List[int]) -> List[int]:
    if direction == "R":
        return [pos[0] + 1, pos[1]]
    elif direction == "L":
        return [pos[0] - 1, pos[1]]
    elif direction == "U":
        return [pos[0], pos[1] + 1]
    elif direction == "D":
        return [pos[0], pos[1] - 1]


DIRECTION_MAP = {"R": (0, 1), "L": (0, -1), "U": (1, 1), "D": (1, -1)}


def _tail_in_range(head: List[int], tail: List[int]) -> bool:
    return head in [
        [tail[0], tail[1]],
        [tail[0] + 1, tail[1]],
        [tail[0] - 1, tail[1]],
        [tail[0], tail[1] + 1],
        [tail[0], tail[1] - 1],
        [tail[0] + 1, tail[1] + 1],
        [tail[0] - 1, tail[1] - 1],
        [tail[0] + 1, tail[1] - 1],
        [tail[0] - 1, tail[1] + 1],
    ]


def rope_positions(
    moves: List[Tuple[Text, int]], tail_length: Optional[int] = 1
) -> int:
    print()
    tail_positions = set()
    snake_size = tail_length + 1
    snake = [[50, 50] for _ in range(snake_size)]
    tail_positions.add(tuple(snake[-1]))
    snake_directions = deque([""] * snake_size, maxlen=snake_size)
    for direction, distance in moves:
        print(direction, distance)
        for g in range(distance):
            snake_directions.appendleft(direction)
            print(direction, g, snake_directions)
            for i in range(len(snake)):
                if i == 0:
                    snake[i] = _move(direction, snake[i])
                    continue
                elif not _tail_in_range(snake[i - 1], snake[i]):
                    print(i, snake[i - 1], snake[i], snake_directions[i - 1])
                    snake[i] = snake[i - 1].copy()
                    coord_position, coord_amount = DIRECTION_MAP[direction]
                    snake[i][coord_position] -= coord_amount
            tail_positions.add(tuple(snake[-1]))
        place_items_on_grid(snake[:-1], snake[-1])
    return len(tail_positions)
