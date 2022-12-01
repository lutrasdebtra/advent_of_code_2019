from year_2022.challenge_1.module import find_highest_calories

with open("one.txt", "r") as ins:
    calories = []
    for line in ins:
        calories.append(line)
    print(find_highest_calories(calories))
    print(find_highest_calories(calories, elves_to_sum=3))
