from year_2023.challenge_12.module import (
    calculate_arrangements,
    calculate_unfolded_arrangements,
)

with open("twelve.txt", "r") as ins:
    records = []
    for line in ins:
        records.append(line.strip())
    print(calculate_arrangements(records=records))
    print(calculate_unfolded_arrangements(records=records))
