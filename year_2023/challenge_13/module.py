from typing import List
import numpy as np


def _process_array(arr: np.array, fix_smudge: bool = False) -> int:
    line_count, _ = arr.shape

    for a, b in ((i, i + 1) for i in range(line_count - 1)):
        smudge_counter = 0
        matching = True
        # Produces tuples of expanding indexes, including the original (a, b): ((3,4), (2,5), (1,6), (0,7)).
        for nxt_a, nxt_b in zip(reversed(range(a + 1)), (range(b, line_count))):
            smudge_counter += np.count_nonzero(arr[nxt_a] != arr[nxt_b])
            if (not fix_smudge and smudge_counter > 0) or (
                fix_smudge and smudge_counter > 1
            ):
                matching = False
                break
        if matching and ((not fix_smudge) or (fix_smudge and smudge_counter == 1)):
            return a + 1
    return 0


def calculate_mirrors(valley: List[str], fix_smudge: bool = False) -> int:
    chunk = []
    np_arrays = []
    valley.append("")
    for line in valley:
        if line == "":
            np_arrays.append(np.array(chunk))
            chunk = []
            continue
        chunk.append(list(line))
    total_result = 0
    for arr in np_arrays:
        total_result += 100 * _process_array(arr, fix_smudge=fix_smudge)
        total_result += _process_array(arr.T, fix_smudge=fix_smudge)
    return total_result
