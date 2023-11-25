class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        msf = 1
        for j in range(1, n):
            for i in range(j):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], dp[i]+1)

            msf = max(msf, dp[j])
        
        return msf