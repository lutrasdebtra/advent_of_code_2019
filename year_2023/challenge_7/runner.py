from year_2023.challenge_7.module import calculate_total_winnings

with open("seven.txt", "r") as ins:
    cards = []
    for line in ins:
        cards.append(line.strip())
    print(calculate_total_winnings(cards=cards, joker_rule=False))
    print(calculate_total_winnings(cards=cards, joker_rule=True))
