import pytest

from year_2023.challenge_20.module import calculate_pulses


@pytest.mark.parametrize(
    "modules, result",
    [
        (
            [
                "broadcaster -> a, b, c",
                "%a -> b",
                "%b -> c",
                "%c -> inv",
                "&inv -> a",
            ],
            32000000,
        ),
        (
            [
                "broadcaster -> a",
                "%a -> inv, con",
                "&inv -> b",
                "%b -> con",
                "&con -> output",
            ],
            11687500,
        ),
    ],
)
def test_calculate_pulses(modules, result):
    assert calculate_pulses(modules=modules) == result
