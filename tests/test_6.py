import pytest

from challenge_6 import count_simple_paths, shortest_path


@pytest.mark.parametrize(
    'file_path, path_count',
    [
        ('data\challenge_6_edge_list.txt', 42),
    ]
)
def test_count_paths(file_path, path_count):
    assert count_simple_paths(file_path) == path_count


@pytest.mark.parametrize(
    'file_path, path_count',
    [
        ('data\challenge_6_edge_list_2.txt', 4),
    ]
)
def test_shortest_path(file_path, path_count):
    assert shortest_path(file_path) == path_count
