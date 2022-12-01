import pytest

from year_2022.challenge_1 import find_highest_calories


@pytest.mark.parametrize(
    "calories, elves_to_sum, max_calories",
    [
        (["1"], 1, 1),
        (["1", "2", "", "1"], 1, 3),
        (["1", "2", "", "1", "4"], 1, 5),
        (["1"], 3, 1),
        (["1", "2", "", "1", "4", "", "1", "", "2"], 3, 10),
    ],
)
def test_find_highest_calories(calories, elves_to_sum, max_calories):
    assert find_highest_calories(calories, elves_to_sum=elves_to_sum) == max_calories
