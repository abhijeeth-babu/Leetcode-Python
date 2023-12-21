class Solution:

    def numIslands(self, grid):
        self.visited = set()
        islands = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and (row, col) not in self.visited:
                    self.dfs(grid, row, col)
                    islands += 1

        return islands

    def dfs(self, mat, r, c):
        if r < 0 or r >= len(mat):
            return

        if c < 0 or c >= len(mat[0]):
            return

        if mat[r][c] == '0':
            return

        if (r, c) in self.visited:
            return
        
        self.visited.add((r, c))
        self.dfs(mat, r+1, c)
        self.dfs(mat, r-1, c)
        self.dfs(mat, r, c+1)
        self.dfs(mat, r, c-1)