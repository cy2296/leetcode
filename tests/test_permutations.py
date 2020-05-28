import pytest

from problems.Permutations import Solution

test_data = [
    ([1,2,3], [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]])
]


@pytest.mark.parametrize("nums, expected", test_data)
def test_permutations(nums, expected):
    sol = Solution()
    result = sol.permute_bfs(nums)
    assert len(result) == len(expected)
    assert not [perm for perm in result if perm not in expected]
