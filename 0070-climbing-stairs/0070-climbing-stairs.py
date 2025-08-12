class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1]*(46)
        def solve(i):
            if i>=n:
                return 1
            if memo[i]!=-1:
                return memo[i]
            one = solve(i+1)
            two = solve(i+2)
            memo[i] = one+two
            return memo[i]
        return solve(1)
