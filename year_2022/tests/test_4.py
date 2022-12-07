import pytest
from year_2022.challenge_4.module import get_subseqs, get_overlaps


@pytest.fixture
def assignments():
    return ["2-4,6-8", "2-3,4-5", "5-7,7-9", "2-8,3-7", "6-6,4-6", "2-6,4-8"]


def test_get_subseqs(assignments):
    assert get_subseqs(assignments) == 2


def test_get_overlaps(assignments):
    assert get_overlaps(assignments) == 4
