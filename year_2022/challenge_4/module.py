from collections import Counter
from typing import List, Text


def _get_seq(elf):
    l = list(map(int, elf.split("-")))
    return list(range(l[0], l[1] + 1))


def _is_subseq(subseq, seq):
    i, n, m = -1, len(seq), len(subseq)
    try:
        while True:
            i = seq.index(subseq[0], i + 1, n - m + 1)
            if subseq == seq[i : i + m]:
                return True
    except ValueError:
        return False


def get_subseqs(assignments: List[Text]) -> int:
    subseqs = 0
    for pair in assignments:
        e_1, e_2 = pair.split(",")
        e_1, e_2 = _get_seq(e_1), _get_seq(e_2)
        if _is_subseq(e_1, e_2) or _is_subseq(e_2, e_1):
            subseqs += 1
    return subseqs


def _has_overlap(seq_1, seq_2):
    seq_1 = Counter(seq_1)
    seq_2 = Counter(seq_2)
    seq_1 &= seq_2
    return bool(list(seq_1.elements()))


def get_overlaps(assignments: List[Text]) -> int:
    overlaps = 0
    for pair in assignments:
        e_1, e_2 = pair.split(",")
        e_1, e_2 = _get_seq(e_1), _get_seq(e_2)
        if _has_overlap(e_1, e_2):
            overlaps += 1
    return overlaps
