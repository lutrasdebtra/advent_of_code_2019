import pytest

from year_2023.challenge_6.module import (
    calculate_total_ways_to_beat_races,
)


@pytest.fixture
def races():
    return [
        "Time:      7  15   30",
        "Distance:  9  40  200",
    ]


@pytest.mark.parametrize(
    "join_races, result",
    [
        (False, 288),
        (True, 71503),
    ],
)
def test_calculate_total_ways_to_beat_races(races, join_races, result):
    assert (
        calculate_total_ways_to_beat_races(races=races, join_races=join_races) == result
    )
