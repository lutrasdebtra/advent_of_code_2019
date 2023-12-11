import pytest

from year_2023.challenge_11.module import (
    calculate_shortest_path_lengths,
)


@pytest.mark.parametrize(
    "expansion, result",
    [
        (2, 374),
        (10, 1030),
        (100, 8410),
    ],
)
def test_calculate_extrapolated_values(expansion, result):
    universe = [
        "...#......",
        ".......#..",
        "#.........",
        "..........",
        "......#...",
        ".#........",
        ".........#",
        "..........",
        ".......#..",
        "#...#.....",
    ]
    assert (
        calculate_shortest_path_lengths(universe=universe, expansion=expansion)
        == result
    )
