import pytest

from helpers import *
from problems.CousinsInBinaryTree import Solution

test_data = [
    ([1, 2, 3, 4], 4, 3, False),
    ([1, 2, 3, None, 4, None, 5], 5, 4, True),
    ([1, 2, 3, None, 4], 2, 3, False)
]
@pytest.mark.parametrize("l, x, y, expected", test_data)
def test_cousins_in_binary_tree_dfs(l, x, y, expected):
    root = list_to_binary_tree(l)
    sol = Solution()
    assert sol.isCousinsDFS(root, x, y) == expected
