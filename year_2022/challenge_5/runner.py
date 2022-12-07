from year_2022.challenge_5.module import crane_controls

with open("five.txt", "r") as ins:
    instructions = []
    for line in ins:
        instructions.append(line)
    print(crane_controls(instructions))
    print(crane_controls(instructions, bulk_move=True))
