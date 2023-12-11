from year_2023.challenge_11.module import (
    calculate_shortest_path_lengths,
)

with open("eleven.txt", "r") as ins:
    universe = []
    for line in ins:
        universe.append(line.strip())
    print(calculate_shortest_path_lengths(universe=universe, expansion=2))
    print(calculate_shortest_path_lengths(universe=universe, expansion=1000000))
