class Solution:
    def uniquePaths(self, m, n):
        if m == 1 and n == 1:
            return 1
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            dp[i][0] = 1
        
        for i in range(1, n):
            dp[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]