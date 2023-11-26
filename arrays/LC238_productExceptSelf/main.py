class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1 for _ in range(n)]

        psf = 1
        for i in range(1, n):
            psf = nums[i-1] * psf
            res[i] = psf

        psf = 1

        for i in range(n-2, -1,-1):
            psf = nums[i+1] * psf
            res[i] *= psf
        
        return res