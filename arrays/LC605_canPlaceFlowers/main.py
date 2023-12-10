from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not flowerbed and n == 0:
            return True
        ln_fb = len(flowerbed)
        for i in range(ln_fb):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == ln_fb-1 or flowerbed[i+1] == 0):
                n -= 1
                flowerbed[i] = 1
            
                if n <= 0:
                    return True
        
        return False