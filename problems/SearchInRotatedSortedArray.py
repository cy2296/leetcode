class Solution:
    """
        two binary searches:
        1. look for the rotation index
        2. define which side the target should be on, then do normal binary search

        Time: O(logN)
        Space: O(1)
    """
    def find_rotation_index(self, nums):
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = lo + (hi-lo) // 2
            if nums[mid] > nums[hi]:
                lo = mid+1
            else:
                hi = mid
        return lo

    def search_1(self, nums, target: int) -> int:
        if not nums:
            return -1

        rot = self.find_rotation_index(nums)
        lo, hi = 0, len(nums)-1

        if target <= nums[hi]:    # target on the right side
            lo = rot
        else:
            hi = rot

        while lo < hi:
            mid = lo + (hi-lo)//2
            if nums[mid] > target:
                lo = mid+1
            else:
                hi = mid

        return lo if nums[lo] == target else -1

    """
        only one binary search is needed
        Time: O(logN)
        Space: O(1)
    """
    def search_2(self, nums, target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mi = lo + (hi - lo) // 2
            if nums[mi] == target:
                return mi
            if nums[lo] <= nums[mi]: # left side sorted
                if nums[lo] <= target <= nums[mi]:
                    hi = mi - 1
                else:
                    lo = mi + 1
            else:                   # right side sorted
                if nums[mi] <= target <= nums[hi]:
                    lo = mi + 1
                else:
                    hi = mi - 1
        return -1


