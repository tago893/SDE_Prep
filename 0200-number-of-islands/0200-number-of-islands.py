class Solution:
    def helper(self,matrix,i,j):
        if i<0 or j<0 or i>=len(matrix) or j>=len(matrix[0]) or matrix[i][j] == '0' or matrix[i][j]=='X':
            return 
        matrix[i][j] = 'X'
        self.helper(matrix, i-1,j)
        self.helper(matrix,i+1,j)
        self.helper(matrix,i,j-1)
        self.helper(matrix,i,j+1)

    def numIslands(self, grid: List[List[str]]) -> int:
        c = 0
        row = len(grid)
        column = len(grid[0]) 
        print(row,column)   
        for i in range(row):
            for j in range(column):
                if grid[i][j] == '1':
                    self.helper(grid,i,j)
                    c+=1

        return c