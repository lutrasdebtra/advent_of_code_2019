from year_2023.challenge_13.module import (
    calculate_mirrors,
)

with open("thirteen.txt", "r") as ins:
    valley = []
    for line in ins:
        valley.append(line.strip())
    print(calculate_mirrors(valley=valley.copy(), fix_smudge=False))
    print(calculate_mirrors(valley=valley.copy(), fix_smudge=True))
