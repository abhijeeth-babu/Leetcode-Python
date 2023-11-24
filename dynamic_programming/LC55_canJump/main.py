class Solution:
    def canJump(self, nums):
        max_distance = 0
        for i in range(len(nums)):
            if max_distance >= i:
                max_distance = max(max_distance, i + nums[i])
            else:
                return False
        return True
            