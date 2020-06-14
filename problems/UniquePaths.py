class Solution:
    """
        Top-Down DP: 1D array
        Time: O(MN)
        Space: O(N)
    """
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    continue
                else:
                    dp[j] += dp[j-1]
        return dp[-1]

    """
        Recursive: Time Limited Exceed
        
        1  1  1  1  1  1  1
        1  2
        1                 x-> sol
        
        dfs(1,1) = dfs(1,0) + dfs(0,1)
        
    """
    def uniquePaths_dfs(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths_dfs(m-1, n) + self.uniquePaths_dfs(m, n-1)
