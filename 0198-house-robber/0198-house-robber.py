class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1]*len(nums)
        n=len(nums)
        def solve(i):
            if i>=n:
                return 0
            if memo[i]!=-1:
                return memo[i]
            memo[i] = max(solve(i+1),nums[i]+solve(i+2))
            return memo[i]
        return solve(0)