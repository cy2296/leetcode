from enum import Enum


class Index(Enum):
    good = 1
    bad = 0
    unknown = -1


class Solution:
    """
        Reference:
        https://leetcode.com/problems/jump-game/solution/

        Backtracking:
        The easiest solution to figure out,
        Most inefficient solution, trying every possible jump pattern that takes
        is from the first position ot the last.

        Time: O(2^N)
        Space: O(N)
    """
    def canJump1(self, nums) -> bool:
        def canJumpFromPosition(pos):
            if pos == len(nums)-1:
                return True

            furthest = min(pos+nums[pos], len(nums)-1)
            for i in range(pos+1, furthest+1):
                if canJumpFromPosition(i):
                    return True
            return False

        return canJumpFromPosition(0)

    """
        Top-Down DP (Optimized backtracking): 
        Same as backtracking except adding a memorization table 
        
        Time limited exceed
        Time: O(N^2)
        Space: O(N)
    """
    def canJump2(self, nums) -> bool:
        def canJumpFromPosition(pos):
            if memo[pos] != Index.unknown:
                return memo[pos] == Index.good

            farthest = min(pos+nums[pos], len(nums)-1)
            for i in range(pos+1, farthest+1):
                if canJumpFromPosition(i):
                    memo[i] = Index.good
                    return True

            memo[pos] = Index.bad
            return False

        memo = [Index.unknown] * len(nums)
        memo[-1] = Index.good
        return canJumpFromPosition(0)

    """
        Bottom-up DP: 
        It's a bit tricky to convert the Top-Down to Bottom-Up solution.
        Practicing similar problems will help bridge the gap
        
        Time Limited Exceed 
        Time: O(N^2)
        Space: O(N)        
    """
    def canJump3(self, nums) -> bool:
        memo = [Index.unknown] * len(nums)
        memo[-1] = Index.good

        for i in range(len(nums)-2, -1, -1):
            furthest = min(len(nums)-1, i+nums[i])
            for j in range(i+1, furthest+1):
                if memo[j] == Index.good:
                    memo[i] = Index.good
                    break

        return memo[0] == Index.good

    """
        Greedy: 
        The perfect Solution! 
        Time: O(N)
        Space: O(1)
    """
    def canJump4(self, nums) -> bool:
        last_pos = len(nums)-1

        for i in range(len(nums)-1, -1, -1):
            if i+nums[i] >= last_pos:
                last_pos = i

        return last_pos == 0
