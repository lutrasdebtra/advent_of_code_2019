from typing import List
import re
from collections import deque
from itertools import pairwise
import operator


def calculate_extrapolated_values(report: List[str], reverse=False) -> int:
    report = [[int(x) for x in re.findall(r"-*\d+", line)] for line in report]
    total_extrapolated_values = 0
    if reverse:
        seq_idx = 0
        operator_func = operator.sub
    else:
        operator_func = operator.add
        seq_idx = -1

    for history in report:
        stack = deque()
        sequence = history
        while len(set(sequence)) > 1:
            new_sequence = []
            for a, b in pairwise(sequence):
                new_sequence.append(b - a)
            stack.append(new_sequence)
            sequence = new_sequence

        diff = 0
        while len(stack):
            sequence = stack.pop()
            diff = operator_func(sequence[seq_idx], diff)

        total_extrapolated_values += operator_func(history[seq_idx], diff)
    return total_extrapolated_values
