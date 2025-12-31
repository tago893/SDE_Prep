class Solution:
    directions = [(-1,0), (1,0), (0,1), (0,-1)]

    def search_word(self, i, j, board, word, k):
        # base case: matched entire word
        if k == len(word):
            return True

        # boundary + mismatch check
        if (
            i < 0 or j < 0 or
            i >= len(board) or j >= len(board[0]) or
            board[i][j] != word[k]
        ):
            return False

        # mark visited
        temp = board[i][j]
        board[i][j] = "#"

        # explore all 4 directions
        for dx, dy in self.directions:
            if self.search_word(i + dx, j + dy, board, word, k + 1):
                return True

        # backtrack
        board[i][j] = temp
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.search_word(i, j, board, word, 0):
                    return True
        return False
