from typing import List
import re
import math


def calculate_total_ways_to_beat_races(
    races: List[str], join_races: bool = False
) -> int:
    for i in range(len(races)):
        if join_races:
            races[i] = races[i].replace(" ", "")
        races[i] = [int(x) for x in re.findall(r"\d+", races[i].split(":")[-1])]
    races = list(zip(races[0], races[1]))

    ways_to_win = []

    for time, distance in races:
        winning_accelerations = 0
        for x in range(1, distance):
            if x * (time - x) > distance:
                winning_accelerations += 1
            # If a new record is not set, but we were setting them previously
            # No more records will be set as the curve is a parabola.
            elif winning_accelerations:
                break
        ways_to_win.append(winning_accelerations)

    return math.prod(ways_to_win)
