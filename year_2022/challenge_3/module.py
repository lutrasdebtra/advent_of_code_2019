from typing import List, Text

PRIORITY_ALPHA = {
    x: idx + 1
    for idx, x in enumerate(
        list(map(chr, range(97, 123))) + list(map(chr, range(65, 91)))
    )
}


def backpack_priorities(backpack_items: List[Text]) -> int:
    total_priorities = 0
    for i in backpack_items:
        half_1, half_2 = set(i[: len(i) // 2]), set(i[len(i) // 2 :])
        shared_items = half_1.intersection(half_2)
        total_priorities += sum(PRIORITY_ALPHA[x] for x in shared_items)
    return total_priorities


def badge_items(backpack_items: List[Text]) -> int:
    total_priorities = 0
    elf_groups = [backpack_items[i : i + 3] for i in range(0, len(backpack_items), 3)]
    for g in elf_groups:
        shared_items = set(g[0]).intersection(set(g[1])).intersection(set(g[2]))
        total_priorities += sum(PRIORITY_ALPHA[x] for x in shared_items)
    return total_priorities
