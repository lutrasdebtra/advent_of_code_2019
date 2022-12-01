from typing import Text, List, Optional
import bisect


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
