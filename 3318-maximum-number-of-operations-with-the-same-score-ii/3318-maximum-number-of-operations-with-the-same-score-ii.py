from functools import lru_cache

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(None)
        def solve(l: int, r: int, target: int) -> int:
            # max ops you can still do on nums[l..r] with required pair sum = target
            if r - l + 1 < 2:
                return 0  # no pair left => no more operations

            best = 0
            # pick first two
            if l + 1 <= r and nums[l] + nums[l + 1] == target:
                best = max(best, 1 + solve(l + 2, r, target))

            # pick last two
            if l <= r - 1 and nums[r - 1] + nums[r] == target:
                best = max(best, 1 + solve(l, r - 2, target))

            # pick first and last
            if nums[l] + nums[r] == target:
                best = max(best, 1 + solve(l + 1, r - 1, target))

            return best

        if n < 2:
            return 0

        # try all three possible first operations to set the target sum
        ans = 0
        ans = max(ans, 1 + solve(2, n - 1, nums[0] + nums[1]))           # first two
        ans = max(ans, 1 + solve(0, n - 3, nums[n - 2] + nums[n - 1]))   # last two
        ans = max(ans, 1 + solve(1, n - 2, nums[0] + nums[n - 1]))       # first + last
        return ans
