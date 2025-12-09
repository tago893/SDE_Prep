class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        def solve(i,combination):
            result.append(combination[:])
            for k in range(i,n):
                combination.append(nums[k])
                solve(k+1,combination)
                combination.pop()
        solve(0,[])
        return result
