class Solution:
    def twoSum(self, nums, target):
        num_map = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], idx]
            num_map[num] = idx
