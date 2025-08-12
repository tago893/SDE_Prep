class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        count = 0
        memo = {}
        def solve(n,num,x):
            if n==0:
                return 1
            if n<0:
                return 0
            if num**x>n:
                return 0
            if (n,num) in memo:
                return memo[(n,num)]
            take = solve(n-num**x,num+1,x)
            skip = solve(n,num+1,x)
            memo[(n,num)] = take+skip
            return memo[(n,num)]
        count = solve(n,1,x)
        return count%(10**9+7)
