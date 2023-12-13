import pytest

from year_2023.challenge_13.module import calculate_mirrors


@pytest.mark.parametrize(
    "fix_smudge, result",
    [
        (False, 405),
        (True, 400),
    ],
)
def test_calculate_mirrors(fix_smudge, result):
    valley = [
        "#.##..##.",
        "..#.##.#.",
        "##......#",
        "##......#",
        "..#.##.#.",
        "..##..##.",
        "#.#.##.#.",
        "",
        "#...##..#",
        "#....#..#",
        "..##..###",
        "#####.##.",
        "#####.##.",
        "..##..###",
        "#....#..#",
    ]
    assert calculate_mirrors(valley=valley, fix_smudge=fix_smudge) == result
