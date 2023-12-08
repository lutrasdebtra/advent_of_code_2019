from year_2023.challenge_8.module import (
    calculate_path_length,
    calculate_simultaneous_path_length,
)

with open("eight.txt", "r") as ins:
    graph = []
    for line in ins:
        graph.append(line.strip())
    print(calculate_path_length(graph=graph))
    print(calculate_simultaneous_path_length(graph=graph))
