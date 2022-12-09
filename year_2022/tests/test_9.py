import pytest
from year_2022.challenge_9.module import rope_positions


@pytest.fixture
def moves_1():
    data = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
    return [(line.split()[0], int(line.split()[-1])) for line in data.splitlines()]


@pytest.fixture
def moves_9():
    data = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""
    return [(line.split()[0], int(line.split()[-1])) for line in data.splitlines()]


def test_rope_positions_tail_length_1(moves_1):
    assert rope_positions(moves_1, tail_length=1) == 13


def test_rope_positions_tail_length_9(moves_9):
    assert rope_positions(moves_9, tail_length=9) == 36
