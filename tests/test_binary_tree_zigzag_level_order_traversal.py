import pytest

from helpers import *
from problems.BinaryTreeZigzagLevelOrderTraversal import Solution

test_data = [
    ([3, 9, 20, None, None, 15, 7], [[3], [20, 9], [15, 7]]),
    ([1, 2, 3, 4, None, None, 5], [[1], [3, 2], [4, 5]])
]


@pytest.mark.parametrize("root, expected", test_data)
def test_binary_tree_zigzag_level_order_traversal_bfs1(root, expected):
    root = list_to_binary_tree(root)
    sol = Solution()
    assert sol.zigzagLevelOrder_bfs1(root) == expected


@pytest.mark.parametrize("root, expected", test_data)
def test_binary_tree_zigzag_level_order_traversal_bfs2(root, expected):
    root = list_to_binary_tree(root)
    sol = Solution()
    assert sol.zigzagLevelOrder_bfs2(root) == expected

@pytest.mark.parametrize("root, expected", test_data)
def test_binary_tree_zigzag_level_order_traversal_dfs(root, expected):
    root = list_to_binary_tree(root)
    sol = Solution()
    assert sol.zigzagLevelOrder_dfs(root) == expected
