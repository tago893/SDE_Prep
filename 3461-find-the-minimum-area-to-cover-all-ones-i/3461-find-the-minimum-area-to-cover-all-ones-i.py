class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        s_row = float("inf")
        s_col = float("inf")

        e_row = float("-inf")
        e_col = float("-inf")
        m = len(grid)
        n = len(grid[0])
        #l to r
        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j] == 1:
                    s_row = min(i,s_row)
                    s_col = min(j,s_col)
                    e_row = max(i,e_row)
                    e_col = max(j,e_col)
                    
        return (e_row-s_row+1) * (e_col-s_col+1)