import pytest

from year_2023.challenge_16.module import (
    calculate_energy,
    calculate_maximum_possible_energy,
)
from typing import List


@pytest.fixture
def mirrors() -> List[str]:
    return r"""
    .|...\....
    |.-.\.....
    .....|-...
    ........|.
    ..........
    .........\
    ..../.\\..
    .-.-/..|..
    .|....-|.\
    ..//.|....
    """.split()


def test_calculate_energy(mirrors):
    assert calculate_energy(mirrors=mirrors) == 46


def test_calculate_maximum_possible_energy(mirrors):
    assert calculate_maximum_possible_energy(mirrors=mirrors) == 51
