from typing import List, Text, Any, Optional
from functools import cmp_to_key


def _packet_order_compare(left: Any, right: Any) -> Optional[bool]:
    # Base Case
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        elif left > right:
            return False
        else:
            return

    if isinstance(left, list) and isinstance(right, int):
        right = [right]
    elif isinstance(left, int) and isinstance(right, list):
        left = [left]

    if isinstance(left, list) and isinstance(right, list):
        comp_len = len(left) if len(left) > len(right) else len(right)
        for i in range(comp_len):
            try:
                left_comp_var = left[i]
            except IndexError:
                return True
            try:
                right_comp_var = right[i]
            except IndexError:
                return False
            compare_result = _packet_order_compare(left_comp_var, right_comp_var)
            if isinstance(compare_result, bool):
                return compare_result


def packet_order(packets: List[Text]) -> int:
    sum_of_right_order = 0
    packets = [eval(p) for p in packets if p.strip() != ""]
    for idx, l in enumerate([packets[i : i + 2] for i in range(0, len(packets), 2)]):
        left, right = l
        if _packet_order_compare(left, right):
            sum_of_right_order += idx + 1
    return sum_of_right_order


def packet_sort(packets: List[Text]) -> int:
    divider_1, divider_2 = [[2]], [[6]]
    packets = [eval(p) for p in packets if p.strip() != ""]
    packets.append(divider_1)
    packets.append(divider_2)

    def make_comparator(f):
        def compare(x, y):
            if f(x, y):
                return -1
            elif f(y, x):
                return 1
            else:
                return 0

        return compare

    packets = sorted(packets, key=cmp_to_key(make_comparator(_packet_order_compare)))
    return (packets.index(divider_1) + 1) * (packets.index(divider_2) + 1)
