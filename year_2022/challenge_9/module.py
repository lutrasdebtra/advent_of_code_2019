from typing import List, Tuple, Text, Optional

sign = lambda x: 1 if x > 0 else (-1 if x < 0 else 0)

DIRECTION_MAP = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}


def rope_positions(
    moves: List[Tuple[Text, int]], tail_length: Optional[int] = 1
) -> int:
    """
    Partial solution taken from: https://github.com/nthistle/advent-of-code/blob/master/2022/day09/day09_p2.py
    """
    tail_positions = set()
    snake_size = tail_length + 1
    snake = [[50, 50] for _ in range(snake_size)]
    tail_positions.add(tuple(snake[-1]))
    for direction, distance in moves:
        for _ in range(distance):
            delta_x, delta_y = DIRECTION_MAP[direction]
            snake[0][0] += delta_x
            snake[0][1] += delta_y
            for i in range(1, len(snake)):
                head_x, head_y = snake[i - 1]
                tail_x, tail_y = snake[i]
                delta_x = tail_x - head_x
                delta_y = tail_y - head_y
                if (abs(delta_x), abs(delta_y)) == (1, 1):
                    continue
                elif delta_x == 0 or delta_y == 0:
                    if abs(delta_x) >= 2:
                        snake[i][0] -= sign(delta_x)
                    if abs(delta_y) >= 2:
                        snake[i][1] -= sign(delta_y)
                else:
                    snake[i][0] -= sign(delta_x)
                    snake[i][1] -= sign(delta_y)
            tail_positions.add(tuple(snake[-1]))
    return len(tail_positions)
