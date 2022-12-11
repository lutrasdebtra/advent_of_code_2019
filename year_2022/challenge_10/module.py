from typing import List, Text


def signal_strength(instructions: List[Text], cycles: List[int]) -> int:
    x = 1
    cycle_count = 0
    signal_strength_amount = 0
    for instruction in instructions:
        instruction = instruction.split(" ")
        instruction_cycles, f = 0, lambda x_tmp: x_tmp
        if instruction[0] == "noop":
            instruction_cycles = 1
        elif instruction[0] == "addx":
            instruction_cycles = 2
            f = lambda x_tmp: x_tmp + int(instruction[1])
        for i in range(instruction_cycles):
            cycle_count += 1
            if cycle_count in cycles:
                signal_strength_amount += cycle_count * x
        x = f(x)
    return signal_strength_amount


def crt_output(instructions: List[Text], cycles: List[int]) -> List[str]:
    cycle_count = 0
    row_count = 0
    sprite_position = [0, 1, 2]
    crt_monitor = [["." for _ in range(40)] for _ in range(len(cycles))]
    for instruction in instructions:
        instruction = instruction.split(" ")
        instruction_cycles, f = 0, lambda l: l
        if instruction[0] == "noop":
            instruction_cycles = 1
        elif instruction[0] == "addx":
            instruction_cycles = 2
            f = lambda l: list(map(lambda x: x + int(instruction[1]), l))
        for i in range(instruction_cycles):
            if row_count in sprite_position:
                crt_monitor[cycle_count // 40][row_count] = "#"
            cycle_count += 1
            row_count += 1
            if row_count == 40:
                row_count = 0
        sprite_position = f(sprite_position)
    return ["".join(line) for line in crt_monitor]
