class Solution:
    def numMagicSquaresInside(self,grid):
        def isMagic(i, j):
            # Check bounds: ensure 3x3 grid fits
            if i + 2 >= len(grid) or j + 2 >= len(grid[0]):
                return False
            
            seen = set()
            # Extract the 3x3 square
            for x in range(3):
                for y in range(3):
                    num = grid[i + x][j + y]
                    if num < 1 or num > 9 or num in seen:
                        return False
                    seen.add(num)
            
            # Now check all row, col, diagonal sums == 15
            # Rows
            for x in range(3):
                if sum(grid[i + x][j + y] for y in range(3)) != 15:
                    return False
            
            # Columns
            for y in range(3):
                if sum(grid[i + x][j + y] for x in range(3)) != 15:
                    return False
            
            # Diagonals
            if (grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] != 15 or
                grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] != 15):
                return False
            
            return True

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if isMagic(i, j):
                    count += 1
        return count