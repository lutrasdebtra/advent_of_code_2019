import pytest

from year_2023.challenge_21.module import calculate_reachable_plots


def test_calculate_reachable_plots():
    garden_plots = [
        "...........",
        ".....###.#.",
        ".###.##..#.",
        "..#.#...#..",
        "....#.#....",
        ".##..S####.",
        ".##..#...#.",
        ".......##..",
        ".##.#.####.",
        ".##..##.##.",
        "...........",
    ]

    assert calculate_reachable_plots(garden_plots=garden_plots, cutoff=6) == 16
