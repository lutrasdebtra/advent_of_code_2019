import pytest

from year_2023.challenge_14.module import calculate_load


@pytest.mark.parametrize(
    "cycles, cycle_directions, result",
    [(1, "N", 136), (1000000000, "NWSE", 64)],
)
def test_calculate_mirrors(cycles, cycle_directions, result):
    rocks = [
        "O....#....",
        "O.OO#....#",
        ".....##...",
        "OO.#O....O",
        ".O.....O#.",
        "O.#..O.#.#",
        "..O..#O..O",
        ".......O..",
        "#....###..",
        "#OO..#....",
    ]
    assert (
        calculate_load(rocks=rocks, cycles=cycles, cycle_directions=cycle_directions)
        == result
    )
