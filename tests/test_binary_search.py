import pytest

from problems.BinarySearch import Solution

test_data = [
    ([-1, 0, 3, 5, 9, 12], 2, -1)
]


@pytest.mark.parametrize("nums, target, expected", test_data)
def test_binary_search(nums, expected, target):
    sol = Solution()
    result = sol.search(nums, target)
    assert result == expected
