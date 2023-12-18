from year_2023.challenge_18.module import calculate_area

with open("eighteen.txt", "r") as ins:
    directions = []
    for line in ins:
        directions.append(line.strip())
    print(calculate_area(directions=directions.copy(), use_hex_instructions=False))
    print(calculate_area(directions=directions.copy(), use_hex_instructions=True))
