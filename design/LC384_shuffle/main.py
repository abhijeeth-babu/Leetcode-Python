import random


class Solution:

    def __init__(self, nums):
        self.arr = nums
        self.org = nums.copy()


    def reset(self):
        self.arr = self.org.copy()
        return self.arr
    
    
    def shuffle(self):
        for idx in range(len(self.arr)):
            ridx = random.randrange(idx, len(self.arr))
            self.arr[idx], self.arr[ridx] = self.arr[ridx], self.arr[idx]
        
        return self.arr