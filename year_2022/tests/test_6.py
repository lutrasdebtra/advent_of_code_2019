import pytest
from year_2022.challenge_6.module import buffer_processor


@pytest.mark.parametrize(
    "communication_stream, marker, pos",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4, 7),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 4, 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 4, 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4, 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4, 11),
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14, 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 14, 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 14, 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14, 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14, 26),
    ],
)
def test_backpack_priorities(communication_stream, marker, pos):
    assert buffer_processor(communication_stream, marker) == pos
