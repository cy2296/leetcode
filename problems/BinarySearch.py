from typing import List

class Solution:
    """
        Ref:
        https://leetcode.com/problems/binary-search/discuss/423162/Binary-Search-101

        Iterative Version 1

        Using higher mid:
            mid = lo + (hi-lo+1)//2
        Exclude mid:
            if nums[mid] > target: hi = mid-1
        Avoid infinitely loop:
            hi = mid-1
    """
    def search_iter1(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = lo + (hi-lo+1)//2
            if nums[mid] > target:
                hi = mid-1
            else:
                lo = mid
        # lo == hi
        return lo if nums[lo] == target else -1

    """
        Iterative Version 2
         
        Using lower mid:
            mid = lo + (hi-lo1)//2
        Exclude mid:
            if nums[mid] < target: lo = mid+1
        Avoid infinitely loop:
            lo = mid+1    
    """
    def search_iter2(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = lo + (hi-lo)//2
            if nums[mid] < target:
                lo = mid+1
            else:
                hi = mid
        # lo == hi
        return lo if nums[lo] == target else -1

    """
        Iteractive version 3
        
        lo <= hi, and check: 
            nums[mid] == target 
        in the while loop        
    """
    def search_iter3(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = lo + (hi-lo)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid+1
            else:
                hi = mid-1
        return -1

    """
        Recursive  
    """
    def search_dfs(self, nums: List[int], target: int) -> int:
        def dfs(lo, hi):
            if lo < hi:
                mid = lo + (hi-lo) // 2
                if nums[mid] < target:
                    return dfs(mid+1, hi)
                else:
                    return dfs(lo, mid)
            return lo if nums[lo] == target else -1

        lo, hi = 0, len(nums)-1
        return dfs(lo, hi)