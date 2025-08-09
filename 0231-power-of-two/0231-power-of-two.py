class Solution:
    # Function to check
    # if x is power of 2
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return False
        return n and not (n & n - 1)
        