from year_2022.challenge_3.module import backpack_priorities, badge_items

with open("three.txt", "r") as ins:
    backpack_items = []
    for line in ins:
        backpack_items.append(line.strip())
    print(backpack_priorities(backpack_items))
    print(badge_items(backpack_items))
