from typing import List, Tuple
import re
from itertools import product
from functools import cache


@cache
def calc_config(
    condition: Tuple[str, ...], groups: Tuple[int, ...], current_group: int = 0
):
    # base cases
    if not condition:
        if current_group:
            return int(len(groups) == 1 and current_group == groups[0])
        else:
            return len(groups) == 0

    if current_group:
        # current group is too long
        if not groups or current_group > groups[0]:
            return 0

    # recursive cases
    if condition[0] == ".":
        # if a group has started
        # then check whether it is the correct length
        # if yes, move onto the next group, or else terminates
        # If a group hasn't started, do nothing
        if current_group:
            if current_group != groups[0]:
                return 0
            else:
                groups = groups[1:]
        return calc_config(condition[1:], groups, 0)
    if condition[0] == "#":
        # increment current group length
        return calc_config(condition[1:], groups, current_group + 1)
    else:
        # this location can either be operational or broken
        if not groups or current_group == groups[0]:
            # if current group length matches the first group in groups
            # or that there are no remaining groups
            # then the current location must be operational
            return calc_config(condition[1:], groups[1:], 0)
        else:
            # if current group length doesn't match the first group in groups
            # and the group has started, then the current location must be broken
            if current_group:
                return calc_config(condition[1:], groups, current_group + 1)
            else:
                # if the group haven't started, then it doesn't have to start now
                return calc_config(
                    condition[1:], groups, current_group + 1
                ) + calc_config(condition[1:], groups, current_group)


def calculate_arrangements(records: List[str]) -> int:
    parsed_records = []
    for record in records:
        spring_condition, spring_numbers = record.split(" ")
        parsed_records.append(
            [
                list(spring_condition),
                list((int(x) for x in re.findall(r"\d+", spring_numbers))),
            ]
        )

    total_arrangements = 0
    for spring_cond, spring_nums in parsed_records:
        arrangements = 0
        missing_data_count = 0
        missing_indexes = []
        for i in range(len(spring_cond)):
            if spring_cond[i] == "?":
                missing_data_count += 1
                missing_indexes.append(i)

        for possible_solution in product("#.", repeat=missing_data_count):
            tmp = spring_cond.copy()
            for idx, i in enumerate(missing_indexes):
                tmp[i] = possible_solution[idx]
            tmp_spring_nums = []
            for group in re.findall(r"\.?(\#+)\.?", "".join(tmp)):
                tmp_spring_nums.append(len(group))

            if tmp_spring_nums == spring_nums:
                arrangements += 1
        total_arrangements += arrangements

    return total_arrangements


def calculate_unfolded_arrangements(records: List[str]) -> int:
    """
    Solution copied from https://old.reddit.com/r/adventofcode/comments/18ge41g/2023_day_12_solutions/kd0ig1u/
    """
    parsed_records = []
    for record in records:
        spring_condition, spring_numbers = record.split(" ")
        parsed_records.append(
            [
                list(spring_condition),
                list((int(x) for x in re.findall(r"\d+", spring_numbers))),
            ]
        )

    for i in range(len(parsed_records)):
        parsed_records[i][0] = (parsed_records[i][0] + ["?"]) * 5
        parsed_records[i][0] = parsed_records[i][0][:-1]
        parsed_records[i][1] = parsed_records[i][1] * 5

    total_arrangements = 0

    for spring_cond, spring_nums in parsed_records:
        total_arrangements += calc_config(tuple(spring_cond), tuple(spring_nums))
    return total_arrangements
