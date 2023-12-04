from year_2023.challenge_4.module import (
    calculate_scratch_card_value,
    calculate_total_scratch_cards,
)

with open("four.txt", "r") as ins:
    scratch_cards = []
    for line in ins:
        scratch_cards.append(line.strip())
    print(calculate_scratch_card_value(scratch_cards=scratch_cards))
    print(calculate_total_scratch_cards(scratch_cards=scratch_cards))
