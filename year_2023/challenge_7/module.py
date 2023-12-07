from typing import List
from collections import Counter


class CamelCardHand:
    hand_types = {
        (5,): 7,  # Five of a kind.
        (1, 4): 6,  # Four of a kind.
        (2, 3): 5,  # Full house.
        (1, 1, 3): 4,  # Three of a kind.
        (1, 2, 2): 3,  # Two pair.
        (1, 1, 1, 2): 2,  # One pair.
        (1, 1, 1, 1, 1): 1,  # High card.
    }

    card_strength = {
        "A": 13,
        "K": 12,
        "Q": 11,
        "J": 10,
        "T": 9,
        "9": 8,
        "8": 7,
        "7": 6,
        "6": 5,
        "5": 4,
        "4": 3,
        "3": 2,
        "2": 1,
    }

    def __init__(self, hand: str):
        self.hand, self.bid = hand.split(" ")
        self.bid = int(self.bid)
        self.hand_type = self._get_hand_type()

    def __eq__(self, other):
        if self.hand_type == other.hand_type:
            return True
        elif self.hand == other.hand:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.hand_type > other.hand_type:
            return True
        elif self.hand_type == other.hand_type:
            for i in range(len(self.hand)):
                if self.hand[i] == other.hand[i]:
                    continue
                else:
                    return (
                        self.card_strength[self.hand[i]]
                        > self.card_strength[other.hand[i]]
                    )
        else:
            return False

    def __repr__(self):
        return f"({self.hand} {self.hand_type})"

    def _get_hand_type(self):
        c = Counter(self.hand)
        return self.hand_types[tuple(sorted(c.values()))]


class CamelCardHandJoker(CamelCardHand):
    card_strength = {
        "A": 13,
        "K": 12,
        "Q": 11,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2,
        "J": 1,
    }

    def _get_hand_type(self):
        c = Counter(self.hand)
        if "J" not in c:
            return self.hand_types[tuple(sorted(c.values()))]
        else:
            jokers_count = c["J"]
            if c["J"] == 5:  # Edge case for JJJJJ.
                return self.hand_types[(5,)]
            # Remove "J" from the counter, then add counts to the other letters starting with the highest number,
            # Making sure not to go above 5.
            del c["J"]
            highest_values = list(sorted(c.values(), reverse=True))
            for i in range(len(highest_values)):
                while jokers_count and highest_values[i] < 5:
                    highest_values[i] += 1
                    jokers_count -= 1
            return self.hand_types[tuple(sorted(highest_values))]


def calculate_total_winnings(cards: List[str], joker_rule: bool = False) -> int:
    if joker_rule:
        camel_card_hands = [CamelCardHandJoker(hand) for hand in cards]
    else:
        camel_card_hands = [CamelCardHand(hand) for hand in cards]
    camel_card_hands.sort()

    total_winnings = 0
    for idx, card in enumerate(camel_card_hands):
        total_winnings += (idx + 1) * card.bid
    return total_winnings
