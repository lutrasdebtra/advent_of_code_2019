import pytest

from year_2023.challenge_3.module import EngineSchematic


@pytest.fixture
def engine_schematic():
    s = """467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598.."""

    return [list(x) for x in s.split()]


def test_sum_part_numbers(engine_schematic):
    assert EngineSchematic(engine_schematic=engine_schematic).sum_part_numbers() == 4361


def test_sum_gear_ratios(engine_schematic):
    assert (
        EngineSchematic(engine_schematic=engine_schematic).sum_gear_ratios() == 467835
    )
