from typing import List

class Solution:
    """
        Top-Down DP: changing the grid inplace
        Time: O(MN)
        Space: O(1)
    """
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0 and j != 0: # first row
                    grid[i][j] += grid[i][j-1]
                elif i != 0 and j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]

    """
        Top-Down DP: using 1-D array to stores the states 
        Time: O(MN)
        Space: O(N)
    """
    def minPathSum_1D(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[0] = grid[0][0]
                elif i == 0 and j != 0:
                    dp[j] = dp[j-1] + grid[i][j]
                elif i != 0 and j == 0:
                    dp[j] += grid[i][j]
                else:
                    dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
        return dp[-1]

