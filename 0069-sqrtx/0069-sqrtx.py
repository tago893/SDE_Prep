class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        l, r = 0, x
        ans = 0
        while l <= r:
            mid = l + (r - l) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square > x:
                r = mid - 1
            else:
                l = mid + 1
                ans = mid  # mid is a valid floor sqrt so far
        return ans