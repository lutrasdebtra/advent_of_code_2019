from functools import reduce


def run_hash_algorithm(init_sequence: str) -> int:
    return sum(
        reduce(lambda acc, s: ((acc + ord(s)) * 17) % 256, seq, 0)
        for seq in init_sequence.split(",")
    )


def calculate_focal_lengths(init_sequence: str) -> int:
    boxes = {x: [] for x in range(256)}
    for instruction in init_sequence.split(","):
        if "-" in instruction:
            label = instruction.split("-")[0]
            label_hash = run_hash_algorithm(init_sequence=label)
            lens_to_remove = None
            for lens in boxes[label_hash]:
                if lens.startswith(label):
                    lens_to_remove = lens
                    break
            if lens_to_remove is not None:
                boxes[label_hash].remove(lens_to_remove)
        elif "=" in instruction:
            label, num = instruction.split("=")
            label_hash = run_hash_algorithm(init_sequence=label)
            new_lens = f"{label} {num}"
            lens_to_replace_idx = None
            for idx, lens in enumerate(boxes[label_hash]):
                if lens.startswith(label):
                    lens_to_replace_idx = idx
                    break
            if lens_to_replace_idx is not None:
                boxes[label_hash][lens_to_replace_idx] = new_lens
            else:
                boxes[label_hash].append(new_lens)

    return sum(
        sum(
            (i + 1) * int(lens.split(" ")[1]) * (idx + 1)
            for idx, lens in enumerate(boxes[i])
        )
        for i in range(256)
    )
