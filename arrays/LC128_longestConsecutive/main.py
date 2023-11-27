class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums)
        lcs = 0
        for num in nums:
            length = 0
            if num - 1 not in num_set:
                while num + length in num_set:
                    length += 1
            lcs = max(lcs, length)

        return lcs   
            