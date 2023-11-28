class Solution:
    def maxSubArray(self, nums):
        curr_sum = nums[0]
        msf = nums[0]

        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum+nums[i])
            msf = max(curr_sum, msf)
        
        return msf