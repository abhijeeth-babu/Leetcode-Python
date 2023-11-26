class Solution:
    def coinChange(self, coins, amount):
        dp = [amount+1] * (amount+1)
        dp[0] = 0

        for amt in range(1, amount+1):
            for coin in coins:
                change = amt - coin
                if change >= 0:
                    dp[amt] = min(
                        1 + dp[change],
                        dp[amt]
                    )
        
        return dp[-1] if dp[-1] != amount + 1 else -1

