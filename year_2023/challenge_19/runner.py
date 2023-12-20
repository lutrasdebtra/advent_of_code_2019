from year_2023.challenge_19.module import (
    calculate_accepted_ratings,
    calculate_possible_accepted_parts,
)

with open("nineteen.txt", "r") as ins:
    workflows = []
    for line in ins:
        workflows.append(line.strip())
    print(calculate_accepted_ratings(workflows=workflows.copy()))
    print(calculate_possible_accepted_parts(workflows=workflows.copy()))
