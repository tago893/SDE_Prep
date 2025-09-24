class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        result = []
        def solve(i,result):
            if i==n:
                result.append(nums[:])
            for j in range(i,n):
                nums[i],nums[j] = nums[j],nums[i]
                solve(i+1,result)
                nums[i],nums[j] = nums[j],nums[i]
        solve(0,result)
        return result