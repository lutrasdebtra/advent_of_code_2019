import re
from typing import List, Text, Optional


SAND_POS = (500, 0)


def sand_counter(rock_coords: List[Text], add_floor: Optional[bool] = False) -> int:
    coords = set()
    deepest_y, widest_x = 0, 0
    grains = 0
    for lines in rock_coords:
        for match in re.finditer(r"(?=(\d{3},\d+\s->\s\d{3},\d+))", lines):
            start, end = match.group(1).split(" -> ")
            x_1, y_1 = map(int, start.split(","))
            x_2, y_2 = map(int, end.split(","))
            ordered_x = sorted([x_1, x_2])
            ordered_y = sorted([y_1, y_2])
            x_coords = list(range(ordered_x[0], ordered_x[-1] + 1))
            y_coords = list(range(ordered_y[0], ordered_y[-1] + 1))
            for x in x_coords:
                for y in y_coords:
                    coords.add((x, y))
                    if x > widest_x:
                        widest_x = x
                    if y > deepest_y:
                        deepest_y = y
    if add_floor:
        floor_y = deepest_y + 2
        for x in range(0, widest_x * 2):
            coords.add((x, floor_y))

    while True:
        sand_x, sand_y = SAND_POS
        while True:
            if not add_floor:
                if sand_y > deepest_y:
                    break
            else:
                if (sand_x, sand_y) in coords:
                    break
            if (sand_x, sand_y + 1) not in coords:
                sand_y += 1
            elif (sand_x, sand_y + 1) in coords and (
                sand_x - 1,
                sand_y + 1,
            ) not in coords:
                sand_y += 1
                sand_x -= 1
            elif (sand_x, sand_y + 1) in coords and (
                sand_x + 1,
                sand_y + 1,
            ) not in coords:
                sand_y += 1
                sand_x += 1
            else:
                coords.add((sand_x, sand_y))
                grains += 1
                break
        if not add_floor:
            if sand_y > deepest_y:
                break
        else:
            if SAND_POS in coords:
                break
    return grains
