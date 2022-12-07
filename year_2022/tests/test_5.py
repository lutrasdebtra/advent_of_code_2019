import pytest
from year_2022.challenge_5.module import crane_controls


@pytest.fixture
def instructions():
    return [
        "    [D]    ",
        "[N] [C]    ",
        "[Z] [M] [P]",
        " 1   2   3 ",
        "",
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2",
    ]


@pytest.mark.parametrize(
    "bulk_move, message",
    [(False, "CMZ"), (True, "MCD")],
)
def test_crane_controls(instructions, bulk_move, message):
    assert crane_controls(instructions, bulk_move=bulk_move) == message
