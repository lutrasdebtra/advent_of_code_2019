import pytest
from year_2022.challenge_3.module import backpack_priorities, badge_items


@pytest.mark.parametrize(
    "rucksack, priority",
    [
        (["vJrwpWtwJgWrhcsFMMfFFhFp"], 16),
        (["jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"], 38),
        (["PmmdzqPrVvPwwTWBwg"], 42),
        (["wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn"], 22),
        (["ttgJtRGJQctTZtZT"], 20),
        (["CrZsJsPPZsGzwwsLwLmpwMDw"], 19),
    ],
)
def test_backpack_priorities(rucksack, priority):
    assert backpack_priorities(rucksack) == priority


@pytest.mark.parametrize(
    "rucksack, priority",
    [
        (
            [
                "vJrwpWtwJgWrhcsFMMfFFhFp",
                "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
                "PmmdzqPrVvPwwTWBwg",
            ],
            18,
        ),
        (
            [
                "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
                "ttgJtRGJQctTZtZT",
                "CrZsJsPPZsGzwwsLwLmpwMDw",
            ],
            52,
        ),
    ],
)
def test_badge_items(rucksack, priority):
    assert badge_items(rucksack) == priority
