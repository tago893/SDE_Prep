class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def solve(i,j,t):
            if i==m-1 and j==n-1:
                return 1
            if i>=m or j>=n:
                return 0
            
            if t[i][j] != -1:
                return t[i][j]
            
            right = solve(i,j+1,t)
            down = solve(i+1,j,t)
            t[i][j] = right + down
            return t[i][j]
        
        t = [[-1 for _ in range(n)]for _ in range(m)]
        return solve(0,0,t)
        