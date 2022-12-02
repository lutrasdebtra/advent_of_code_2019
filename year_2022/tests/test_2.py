import pytest
from year_2022.challenge_2.module import calculate_tournament_1, calculate_tournament_2


@pytest.mark.parametrize(
    "encrypted_guide, final_score",
    [
        ([("A", "Y")], 8),
        ([("B", "X")], 1),
        ([("C", "Z")], 6),
        ([("A", "Y"), ("B", "X"), ("C", "Z")], 15),
    ],
)
def test_calculate_tournament_1(encrypted_guide, final_score):
    assert calculate_tournament_1(encrypted_guide) == final_score


@pytest.mark.parametrize(
    "encrypted_guide, final_score",
    [
        ([("A", "Y")], 4),
        ([("B", "X")], 1),
        ([("C", "Z")], 7),
        ([("A", "Y"), ("B", "X"), ("C", "Z")], 12),
    ],
)
def test_calculate_tournament_2(encrypted_guide, final_score):
    assert calculate_tournament_2(encrypted_guide) == final_score
