import pytest

from year_2023.challenge_17.module import calculate_shortest_distance

city_block_example_1 = [
    "2413432311323",
    "3215453535623",
    "3255245654254",
    "3446585845452",
    "4546657867536",
    "1438598798454",
    "4457876987766",
    "3637877979653",
    "4654967986887",
    "4564679986453",
    "1224686865563",
    "2546548887735",
    "4322674655533",
]

city_block_example_2 = [
    "111111111111",
    "999999999991",
    "999999999991",
    "999999999991",
    "999999999991",
]


@pytest.mark.parametrize(
    "city_blocks, ultra, result",
    [
        (city_block_example_1, False, 102),
        (city_block_example_1, True, 94),
        (city_block_example_2, True, 71),
    ],
)
def test_calculate_shortest_distance_non_ultra(city_blocks, ultra, result):
    assert calculate_shortest_distance(city_blocks=city_blocks, ultra=ultra) == result
