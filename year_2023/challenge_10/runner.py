from year_2023.challenge_10.module import (
    calculate_farthest_point,
    calculate_cycle_cover,
)

with open("ten.txt", "r") as ins:
    pipes = []
    for line in ins:
        pipes.append(line.strip())
    print(calculate_farthest_point(pipes=pipes))
    print(calculate_cycle_cover(pipes=pipes))
