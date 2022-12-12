import pytest
from year_2022.challenge_12.module import hill_climb


@pytest.fixture
def elevations():
    data = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""
    return [list(line) for line in data.splitlines()]


@pytest.mark.parametrize(
    "source, steps",
    [
        ("S", 31),
        ("a", 29),
    ],
)
def test_hill_climb(source, steps, elevations):
    assert hill_climb(elevations, source=source) == steps
