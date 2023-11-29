from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(nums, r, f):
            if len(r) == len(nums):
                # appending a copy into final
                f.append(r.copy())
                return
            
            for num in nums:
                if num not in r:
                    # backtracking
                    r.append(num)
                    helper(nums, r, f)
                    r.pop()
            
        f =  []
        for num in nums:
            helper(nums, [num], f)
        return f

sol = Solution()
print(sol.permute([1,2,3]))