import pytest
from year_2022.challenge_14.module import sand_counter


@pytest.fixture
def rock_coords():
    data = """498,4 -> 498,6 -> 496,6
    503,4 -> 502,4 -> 502,9 -> 494,9"""
    return data.splitlines()


@pytest.mark.parametrize(
    "add_floor, grains",
    [
        (False, 24),
        (True, 93),
    ],
)
def test_sand_counter(add_floor, grains, rock_coords):
    assert sand_counter(rock_coords, add_floor=add_floor) == grains
