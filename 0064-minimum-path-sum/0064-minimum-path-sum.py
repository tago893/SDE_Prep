class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        dp = [[-1 for _ in range(n)]for _ in range(m)]

        def solve(i,j,dp):
            if i<0 or j<0 or i>=m or j>=n:
                return float("inf")
            if dp[i][j] != -1:
                return dp[i][j]
            if i == m-1 and j == n-1:
                return grid[i][j]
            right = solve(i,j+1,dp)
            down  = solve(i+1,j,dp)

            dp[i][j] = grid[i][j] + min(right,down)
            return dp[i][j]
        return solve(0,0,dp)
            

