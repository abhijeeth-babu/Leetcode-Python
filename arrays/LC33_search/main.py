class Solution:
    def search(self, nums, target):
        # get the index of actual smallest element if sorted correctly
        k = self.get_index(nums)

        l, r, n = 0, len(nums) - 1, len(nums)

        while l <= r:
            m = (l + r) // 2
            # shift m so that we know the value of mth position if array was sorted
            m_s = (m + k) % n
            if nums[m_s] == target:
                return m_s
            elif nums[m_s] > target:
                r = m - 1
            else:
                l = m + 1
        
        return -1

    def get_index(self, nums):
        l, r = 0, len(nums) - 1
        if nums[l] < nums[r]:
            return 0
        
        while l < r:
            m = (l + r) // 2
            if nums[m-1] > nums[m] and nums[m+1] > nums[m]:
                return m
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1

        return l