import pytest

from year_2023.challenge_7.module import calculate_total_winnings


@pytest.fixture
def cards():
    return ["32T3K 765", "T55J5 684", "KK677 28", "KTJJT 220", "QQQJA 483"]


@pytest.mark.parametrize(
    "joker_rule, result",
    [
        (False, 6440),
        (True, 5905),
    ],
)
def test_calculate_total_ways_to_beat_races(cards, joker_rule, result):
    assert calculate_total_winnings(cards=cards, joker_rule=joker_rule) == result
