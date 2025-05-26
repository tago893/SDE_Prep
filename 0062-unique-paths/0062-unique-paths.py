class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def solve(i,j,t):
            #Valid path
            if i==m-1 and j==n-1:
                return 1
            #Not valid path
            if i<0 or j>=n or i>=m:
                return 0
            
            if t[i][j] != -1:
                return t[i][j]
            right = solve(i,j+1,t)
            down = solve(i+1,j,t)

            t[i][j]=right+down
            return t[i][j] 
        
        t=[[-1 for _ in range(n+1)]for _ in range(m+1)]
        return solve(0,0,t)
        