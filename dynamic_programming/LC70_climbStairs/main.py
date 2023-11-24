class Solution:
    dp = {}
    def climbStairs(self, n):
        if n <= 3:
            return n
        elif n in self.dp:
            return self.dp[n]
        else:
            self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.dp[n]

