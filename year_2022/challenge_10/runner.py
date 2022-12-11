from year_2022.challenge_10.module import signal_strength, crt_output

with open("ten.txt", "r") as ins:
    instructions = []
    for line in ins:
        instructions.append(line.strip())
    print(signal_strength(instructions, [20, 60, 100, 140, 180, 220]))
    lines = crt_output(instructions, [40, 80, 120, 160, 200, 240])
    print()
    for line in lines:
        print(line)
