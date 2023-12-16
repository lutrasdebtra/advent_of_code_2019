from year_2023.challenge_16.module import (
    calculate_energy,
    calculate_maximum_possible_energy,
)

with open("sixteen.txt", "r") as ins:
    mirrors = []
    for line in ins:
        mirrors.append(line.strip())
    # print(calculate_energy(mirrors=mirrors.copy()))
    print(calculate_maximum_possible_energy(mirrors=mirrors.copy()))
