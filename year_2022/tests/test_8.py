import pytest
from year_2022.challenge_8.module import visible_trees, scenic_score


@pytest.fixture
def adjacency_matrix():
    data = """30373
    25512
    65332
    33549
    35390"""
    return [[int(x) for x in row.strip()] for row in data.splitlines()]


def test_visible_trees(adjacency_matrix):
    assert visible_trees(adjacency_matrix) == 21


def test_scenic_score(adjacency_matrix):
    assert scenic_score(adjacency_matrix) == 8
