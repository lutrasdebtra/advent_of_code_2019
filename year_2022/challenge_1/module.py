from typing import Text, List, Optional
import bisect
from itertools import groupby


def find_highest_calories(calories: List[Text], elves_to_sum: Optional[int] = 1) -> int:
    elves = []
    calorie_counter = 0
    for line in calories + [""]:
        try:
            calorie_counter += int(line)
        except ValueError:
            bisect.insort(elves, calorie_counter)
            calorie_counter = 0
    return sum(elves[-elves_to_sum:])


def find_highest_calories_one_line(
    calories: List[Text], elves_to_sum: Optional[int] = 1
) -> int:
    return sum(
        sorted(
            [
                sum([int(n.strip()) for n in x])
                for x in [
                    list(g)
                    for k, g in groupby(calories, key=lambda x: x.strip() != "")
                    if k
                ]
            ]
        )[-elves_to_sum:]
    )
