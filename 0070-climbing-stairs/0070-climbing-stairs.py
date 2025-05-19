class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1]*(n)
        if n==0 or n==1:
            return 1
        if n==2:
            return 2
        def dfs(i):
            if i>=n:
                return 1
            
            if memo[i]!=-1:
                return memo[i]
            memo[i]=dfs(i+1)+dfs(i+2)
            return memo[i]
        result = dfs(1)
        return result