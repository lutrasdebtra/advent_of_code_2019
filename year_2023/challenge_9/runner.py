from year_2023.challenge_9.module import (
    calculate_extrapolated_values,
)

with open("nine.txt", "r") as ins:
    report = []
    for line in ins:
        report.append(line.strip())
    print(calculate_extrapolated_values(report=report, reverse=False))
    print(calculate_extrapolated_values(report=report, reverse=True))
