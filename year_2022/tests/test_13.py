import pytest
from year_2022.challenge_13.module import packet_order, packet_sort


@pytest.fixture
def packets():
    data = """[1,1,3,1,1]
    [1,1,5,1,1]

    [[1],[2,3,4]]
    [[1],4]

    [9]
    [[8,7,6]]

    [[4,4],4,4]
    [[4,4],4,4,4]

    [7,7,7,7]
    [7,7,7]

    []
    [3]

    [[[]]]
    [[]]

    [1,[2,[3,[4,[5,6,7]]]],8,9]
    [1,[2,[3,[4,[5,6,0]]]],8,9]
    """
    return data.splitlines()


def test_packet_order(packets):
    assert packet_order(packets) == 13


def test_packet_sort(packets):
    assert packet_sort(packets) == 140
