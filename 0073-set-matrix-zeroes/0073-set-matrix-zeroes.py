class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row = False
        first_col = False
        m = len(matrix)
        n= len(matrix[0])
        
        for i in range(0,m):
            for j in range(0,n):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row = True
                    if j == 0:
                        first_col = True
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]== 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if first_row:
            for j in range(0,n):
                matrix[0][j] = 0
        if first_col:
            for i in range(0,m):
                matrix[i][0] = 0

        