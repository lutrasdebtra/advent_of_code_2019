from year_2023.challenge_20.module import calculate_pulses, calculate_presses_to_rx

with open("twenty.txt", "r") as ins:
    modules = []
    for line in ins:
        modules.append(line.strip())
    # print(calculate_pulses(modules=modules))
    print(calculate_presses_to_rx(modules=modules))
