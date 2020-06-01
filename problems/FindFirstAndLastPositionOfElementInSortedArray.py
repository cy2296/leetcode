from typing import List


class Solution:
    """
        Implement two binary search, one search for lower bound, the other search for upper bound
    """
    def _binary_search_lower_bound(self, nums, target):
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = lo + (hi-lo) // 2
            if nums[mid] < target:
                lo = mid+1
            else:
                hi = mid
        return lo           # lo == hi

    def _binary_search_upper_bound(self, nums, target):
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = lo + (hi-lo+1)//2
            if nums[mid] > target:
                hi = mid-1
            else:
                lo = mid
        return hi           # hi == lo

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo = self._binary_search_lower_bound(nums, target)
        if lo == len(nums) or nums[lo] != target:
            return [-1, -1]
        hi = self._binary_search_upper_bound(nums, target)
        return [lo, hi]


