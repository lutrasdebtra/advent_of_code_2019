import pytest

from year_2023.challenge_9.module import (
    calculate_extrapolated_values,
)


@pytest.mark.parametrize(
    "reverse, result",
    [
        (False, 114),
        (True, 2),
    ],
)
def test_calculate_extrapolated_values(reverse, result):
    report = ["0 3 6 9 12 15", "1 3 6 10 15 21", "10 13 16 21 30 45"]
    assert calculate_extrapolated_values(report=report, reverse=reverse) == result
