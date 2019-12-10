def _instruction_1(instructions, pos):
    pos_1, pos_2, pos_3 = instructions[pos + 1], instructions[pos + 2], instructions[pos + 3]
    instructions[pos_3] = instructions[pos_1] + instructions[pos_2]
    pos += 3
    return instructions, pos


def _instruction_2(instructions, pos):
    pos_1, pos_2, pos_3 = instructions[pos + 1], instructions[pos + 2], instructions[pos + 3]
    instructions[pos_3] = instructions[pos_1] * instructions[pos_2]
    pos += 3
    return instructions, pos


def run_intcode(intcode_string):
    instructions = [int(x) for x in intcode_string.split(',')]
    pos = -1
    while pos < len(instructions):
        pos += 1
        opt_code = instructions[pos]
        if opt_code == 99:
            break
        if opt_code == 1:
            instructions, pos = _instruction_1(instructions, pos)
        elif opt_code == 2:
            instructions, pos = _instruction_2(instructions, pos)
    return instructions
