class Solution:
    def spiralOrder(self, matrix):
        res = []
        top, bottom = 0, len(matrix) - 1 # rows
        left, right = 0, len(matrix[0]) - 1 # columns

        direction = "right"
        while top <= bottom and left <= right:
            if direction == "right":
                for i in range(left, right+1):
                    res.append(matrix[top][i])
                direction = "down"
                top += 1
            elif direction == "down":
                for i in range(top, bottom + 1):
                    res.append(matrix[i][right])
                direction = "left"
                right -= 1
            elif direction == "left":
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                direction = "up"
                bottom -= 1
            elif direction == "up":
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                direction = "right"
                left += 1
        
        return res
    
obj = Solution()
print(obj.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))