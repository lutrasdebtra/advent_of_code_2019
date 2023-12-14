from year_2023.challenge_14.module import (
    calculate_load,
)

with open("fourteen.txt", "r") as ins:
    rocks = []
    for line in ins:
        rocks.append(line.strip())
    print(calculate_load(rocks=rocks.copy(), cycles=1, cycle_directions="N"))
    print(
        calculate_load(rocks=rocks.copy(), cycles=1000000000, cycle_directions="NWSE")
    )
