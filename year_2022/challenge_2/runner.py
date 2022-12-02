from year_2022.challenge_2.module import calculate_tournament_1, calculate_tournament_2

with open("two.txt", "r") as ins:
    encrypted_guide = []
    for line in ins:
        encrypted_guide.append(tuple(x.strip() for x in line.split()))
    print(calculate_tournament_1(encrypted_guide))
    print(calculate_tournament_2(encrypted_guide))
