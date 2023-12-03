from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board, row, col, count, word):
            nonlocal found
            if not ((0 <= row < len(board)) and (0 <= col < len(board[0]))):
                return
            
            if board[row][col] != word[count]:
                return
            
            if count == len(word) - 1 and word[count] == board[row][col]:
                found = True
                return
            
            current = board[row][col]
            board[row][col] = ""
            dfs(board, row+1, col, count+1, word)
            dfs(board, row-1, col, count+1, word)
            dfs(board, row, col+1, count+1, word)
            dfs(board, row, col-1, count+1, word)
            board[row][col] = current

        found = False
        count = 0

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[count]:
                    dfs(board, row, col, count, word)

        return found