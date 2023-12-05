class NumArray:

    def __init__(self, nums):
        self.cumsum = nums
        for i in range(1, len(nums)):
            self.cumsum[i] += self.cumsum[i-1]
        

    def sumRange(self, i, j):
        if i > 0:
            return self.cumsum[j] - self.cumsum[i-1]
        else:
            return self.cumsum[j]
        
