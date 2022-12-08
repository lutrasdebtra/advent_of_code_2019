from typing import List, Tuple


def _is_leaf(x: int, y: int, size: int) -> bool:
    return x in [0, size - 1] or y in [0, size - 1]


def _generate_paths(x: int, y: int, size: int) -> List[List[Tuple[int, int]]]:
    return [
        list(reversed([(x_2, y) for x_2 in range(0, x)])),  # left.
        [(x_2, y) for x_2 in range(x + 1, size)],  # right.
        list(reversed([(x, y_2) for y_2 in range(0, y)])),  # up.
        [(x, y_2) for y_2 in range(y + 1, size)],  # down.
    ]


def visible_trees(adjacency_matrix: List[List[int]]) -> int:
    visible_trees_count = 0
    size = len(adjacency_matrix)
    for x in range(size):
        for y in range(size):
            if _is_leaf(x, y, size):
                visible_trees_count += 1
                continue
            tree = adjacency_matrix[x][y]
            visible = [True, True, True, True]
            for idx, path in enumerate(_generate_paths(x, y, size)):
                for x_2, y_2 in path:
                    neighbour = adjacency_matrix[x_2][y_2]
                    if neighbour >= tree:
                        visible[idx] = False
            if any(visible):
                visible_trees_count += 1
    return visible_trees_count


def scenic_score(adjacency_matrix: List[List[int]]) -> int:
    size = len(adjacency_matrix)
    max_scenic_score = 1
    for x in range(size):
        for y in range(size):
            if _is_leaf(x, y, size):
                continue
            tree_scenic_score = 1
            tree = adjacency_matrix[x][y]
            for path in _generate_paths(x, y, size):
                visible_trees = 0
                for x_2, y_2 in path:
                    neighbour = adjacency_matrix[x_2][y_2]
                    visible_trees += 1
                    if neighbour >= tree:
                        break
                tree_scenic_score *= visible_trees
            max_scenic_score = (
                max_scenic_score
                if max_scenic_score > tree_scenic_score
                else tree_scenic_score
            )
    return max_scenic_score
