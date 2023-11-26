class Solution:
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        max_vol = 0
        max_ht = max(height)
        while l < r:
            if max_ht * (r - l) < max_vol: # optimization / not necessary
                return max_vol
            current_vol = min(height[l], height[r]) * (r - l)
            max_vol = max(current_vol, max_vol)
            if height[l] >= height[r]:
                r -= 1
            else:
                l += 1

        return max_vol
            