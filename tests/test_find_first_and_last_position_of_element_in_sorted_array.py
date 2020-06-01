import pytest

from problems.FindFirstAndLastPositionOfElementInSortedArray import Solution

test_data = [
    ([], 0, [-1, -1]),
    # ([5, 7, 7, 8, 8, 10], 8, [3, 4])

]
@pytest.mark.parametrize("nums, target, expected", test_data)
def test_find_first_and_last_position_of_element_in_sorted_array(nums, expected, target):
    sol = Solution()
    result = sol.searchRange(nums, target)
    assert result == expected