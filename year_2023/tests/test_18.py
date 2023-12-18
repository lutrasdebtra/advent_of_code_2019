import pytest

from year_2023.challenge_18.module import calculate_area


@pytest.mark.parametrize(
    "use_hex_instructions, result",
    [(False, 62), (True, 952408144115)],
)
def test_calculate_area(use_hex_instructions, result):
    directions = [
        "R 6 (#70c710)",
        "D 5 (#0dc571)",
        "L 2 (#5713f0)",
        "D 2 (#d2c081)",
        "R 2 (#59c680)",
        "D 2 (#411b91)",
        "L 5 (#8ceee2)",
        "U 2 (#caa173)",
        "L 1 (#1b58a2)",
        "U 2 (#caa171)",
        "R 2 (#7807d2)",
        "U 3 (#a77fa3)",
        "L 2 (#015232)",
        "U 2 (#7a21e3)",
    ]

    assert (
        calculate_area(directions=directions, use_hex_instructions=use_hex_instructions)
        == result
    )
