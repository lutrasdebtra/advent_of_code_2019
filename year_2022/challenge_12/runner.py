from year_2022.challenge_12.module import hill_climb

with open("twelve.txt", "r") as ins:
    elevations = []
    for line in ins:
        elevations.append(list(line.strip()))
    print(hill_climb(elevations))
    print(hill_climb(elevations, source="a"))
