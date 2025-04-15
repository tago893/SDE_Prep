class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i>=len(nums):
                res.append(subset.copy())
                return
            # DECISION TO TAKE
            subset.append(nums[i])
            dfs(i+1)
            # DECISION TO NOT TAKE
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res