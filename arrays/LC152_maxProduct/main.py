class Solution:
    def maxProduct(self, nums):
        curr_max = nums[0]
        curr_min = nums[0]
        msf = max(curr_max, curr_min)
        for i in range(1, len(nums)):
            a = nums[i]
            b = curr_max * nums[i]
            c = curr_min * nums[i]
            curr_max = max(
                a,
                b,
                c
            )
            curr_min = min(
                a,
                b,
                c
            )
            msf = max(msf, curr_max)
        
        return msf
