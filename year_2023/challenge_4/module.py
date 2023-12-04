from typing import List, Set, Tuple
import re


def _parse_scratch_card(scratch_card: str) -> Tuple[int, Set[int]]:
    game_id, numbers = scratch_card.split(":")
    game_id = int(game_id.split(" ")[-1])
    game_numbers, winning_numbers = numbers.split("|")
    game_numbers = set(int(x) for x in re.findall(r"\d+", game_numbers))
    winning_numbers = set(int(x) for x in re.findall(r"\d+", winning_numbers))
    matches = game_numbers.intersection(winning_numbers)

    return game_id, matches


def calculate_scratch_card_value(scratch_cards: List[str]) -> int:
    winning_points = 0
    for scratch_card in scratch_cards:
        _, matches = _parse_scratch_card(scratch_card=scratch_card)
        if matches:
            winning_points += 2 ** (len(matches) - 1)
    return winning_points


def calculate_total_scratch_cards(scratch_cards: List[str]) -> int:
    total_scratch_cards = 0
    card_counter = {x: 1 for x in range(len(scratch_cards))}
    for scratch_card in scratch_cards:
        game_id, matches = _parse_scratch_card(scratch_card=scratch_card)
        # Repeat the win process for the number of duplicates of each game.
        for _ in range(card_counter[game_id - 1]):
            total_scratch_cards += 1
            if matches:
                # Game_id is index + 1 already, so we can start there.
                for i in range(game_id, game_id + len(matches)):
                    card_counter[i] += 1
    return total_scratch_cards
