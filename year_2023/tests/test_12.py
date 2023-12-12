import pytest

from year_2023.challenge_12.module import (
    calculate_arrangements,
    calculate_unfolded_arrangements,
)


@pytest.fixture
def records():
    return [
        "???.### 1,1,3",
        ".??..??...?##. 1,1,3",
        "?#?#?#?#?#?#?#? 1,3,1,6",
        "????.#...#... 4,1,1",
        "????.######..#####. 1,6,5",
        "?###???????? 3,2,1",
    ]


def test_calculate_arrangements(records):
    assert calculate_arrangements(records=records) == 21


def test_calculate_unfolded_arrangements(records):
    assert calculate_unfolded_arrangements(records=records) == 525152
