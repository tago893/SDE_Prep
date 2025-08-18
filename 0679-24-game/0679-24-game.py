from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPS = 1e-6  # tolerance for floating point

        def solve(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPS

            n = len(nums)
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    # pick two numbers
                    a, b = nums[i], nums[j]

                    # possible results
                    next_vals = set()
                    next_vals.add(a + b)
                    next_vals.add(a - b)
                    next_vals.add(b - a)
                    next_vals.add(a * b)
                    if abs(b) > EPS:  # avoid div by 0
                        next_vals.add(a / b)
                    if abs(a) > EPS:
                        next_vals.add(b / a)

                    # remaining numbers
                    rem = [nums[k] for k in range(n) if k not in (i, j)]

                    # try each result with recursion
                    for val in next_vals:
                        if solve(rem + [val]):
                            return True
            return False

        return solve([float(c) for c in cards])
