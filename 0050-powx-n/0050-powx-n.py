class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def solve(x,n):
            if n==0:
                return 1.0
            result = solve(x,n//2)
            if n%2 == 1:
                return x*result*result
            return result*result
            
        ans = 0
        if n<0:
            return solve(1.0/x,-n)
        elif n==0:
            return 1.0
        else:
            return solve(x,n)
        
        