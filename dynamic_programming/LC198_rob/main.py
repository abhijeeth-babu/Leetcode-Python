class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[-1]
        dp = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            dp.append(
                max(dp[i-2]+nums[i], dp[i-1])
            )
        return dp[-1]