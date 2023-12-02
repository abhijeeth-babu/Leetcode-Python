class Solution:
    def setZeroes(self, matrix):
        first_row_has_zero = False
        first_col_has_zero = False
        rows, cols = len(matrix), len(matrix[0])

        for col in range(cols):
            if matrix[0][col] == 0:
                first_row_has_zero = True
                break

        for row in range(rows):
            if matrix[row][0] == 0:
                first_col_has_zero = True
                break
        
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
        
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0

        if first_row_has_zero:
            for row in range(rows):
                matrix[row][0] = 0
        
        if first_col_has_zero:
            for col in range(cols):
                matrix[0][col] = 0