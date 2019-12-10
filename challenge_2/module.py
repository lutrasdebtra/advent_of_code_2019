def run_intcode(intcode_string):
    instructions = [int(x) for x in intcode_string.split(',')]
    for i in range(0, len(instructions), 4):
        if i + 3 > len(instructions):
            break
        first_instruction = instructions[i]
        pos_1, pos_2, pos_3 = instructions[i+1], instructions[i+2], instructions[i+3]
        if first_instruction == 99:
            break
        elif first_instruction == 1:
            instructions[pos_3] = instructions[pos_1] + instructions[pos_2]
        elif first_instruction == 2:
            instructions[pos_3] = instructions[pos_1] * instructions[pos_2]
    return instructions
