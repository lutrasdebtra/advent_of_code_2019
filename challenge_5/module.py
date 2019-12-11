def _instruction_1(instructions, pos, immediate_modes):
    pos_1, pos_2, pos_3 = instructions[pos + 1], instructions[pos + 2], instructions[pos + 3]
    instructions[pos_3] = _get_instruction(instructions, pos_1, value_mode=(0 in immediate_modes)) + \
                          _get_instruction(instructions, pos_2, value_mode=(1 in immediate_modes))
    pos += 4
    return instructions, pos


def _instruction_2(instructions, pos, immediate_modes):
    pos_1, pos_2, pos_3 = instructions[pos + 1], instructions[pos + 2], instructions[pos + 3]
    instructions[pos_3] = _get_instruction(instructions, pos_1, value_mode=(0 in immediate_modes)) * \
                          _get_instruction(instructions, pos_2, value_mode=(1 in immediate_modes))
    pos += 4
    return instructions, pos


def _instruction_3(instructions, pos, input_):
    if input_:
        pos_1 = instructions[pos + 1]
        instructions[pos_1] = input_
    pos += 2
    return instructions, pos


def _instruction_4(instructions, pos):
    pos_1 = instructions[pos + 1]
    pos += 2
    return instructions, pos, instructions[pos_1]


def _instruction_5(instructions, pos, immediate_modes):
    pos_1, pos_2 = instructions[pos + 1], instructions[pos + 2]
    if _get_instruction(instructions, pos_1, value_mode=(0 in immediate_modes)) != 0:
        pos = _get_instruction(instructions, pos_2, value_mode=(1 in immediate_modes))
    else:
        pos += 3
    return instructions, pos


def _instruction_6(instructions, pos, immediate_modes):
    pos_1, pos_2 = instructions[pos + 1], instructions[pos + 2]
    if _get_instruction(instructions, pos_1, value_mode=(0 in immediate_modes)) == 0:
        pos = _get_instruction(instructions, pos_2, value_mode=(1 in immediate_modes))
    else:
        pos += 3
    return instructions, pos


def _instruction_7(instructions, pos, immediate_modes):
    pos_1, pos_2, pos_3 = instructions[pos + 1], instructions[pos + 2], instructions[pos + 3]
    if _get_instruction(instructions, pos_1, value_mode=(0 in immediate_modes)) < \
            _get_instruction(instructions, pos_2, value_mode=(1 in immediate_modes)):
        instructions[pos_3] = 1
    else:
        instructions[pos_3] = 0
    pos += 4
    return instructions, pos


def _instruction_8(instructions, pos, immediate_modes):
    pos_1, pos_2, pos_3 = instructions[pos + 1], instructions[pos + 2], instructions[pos + 3]
    if _get_instruction(instructions, pos_1, value_mode=(0 in immediate_modes)) == \
            _get_instruction(instructions, pos_2, value_mode=(1 in immediate_modes)):
        instructions[pos_3] = 1
    else:
        instructions[pos_3] = 0
    pos += 4
    return instructions, pos


def _get_instruction(instructions, position, value_mode=False):
    if value_mode:
        return position
    return instructions[position]


def process_opt_code(opt_code):
    opt_code_str = str(opt_code)
    immediate_modes = set()
    parameters_, mode_ = opt_code_str[:-2], int(opt_code_str[-2:])

    for i, v in enumerate(reversed(parameters_)):
        if int(v) == 1:
            immediate_modes.add(i)
    return mode_, immediate_modes


def run_intcode(intcode_string, input_=None):
    instructions = [int(x) for x in intcode_string.split(',')]
    pos = 0
    while pos < len(instructions):
        opt_code, immediate_modes = process_opt_code(instructions[pos])
        if opt_code == 99:
            break
        if opt_code == 1:
            instructions, pos = _instruction_1(instructions, pos, immediate_modes)
        elif opt_code == 2:
            instructions, pos = _instruction_2(instructions, pos, immediate_modes)
        elif opt_code == 3:
            instructions, pos = _instruction_3(instructions, pos, input_)
        elif opt_code == 4:
            instructions, pos, output_ = _instruction_4(instructions, pos)
            print(output_)
        elif opt_code == 5:
            instructions, pos = _instruction_5(instructions, pos, immediate_modes)
        elif opt_code == 6:
            instructions, pos = _instruction_6(instructions, pos, immediate_modes)
        elif opt_code == 7:
            instructions, pos = _instruction_7(instructions, pos, immediate_modes)
        elif opt_code == 8:
            instructions, pos = _instruction_8(instructions, pos, immediate_modes)
    return instructions
