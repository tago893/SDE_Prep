class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        result = []
        def solve(i,result):
            if i==n:
                result.append(nums[:])
            s = set()
            for j in range(i,n):
                if nums[j] in s: # takes care of duplicate swap
                    continue
                s.add(nums[j])
                nums[i],nums[j] = nums[j],nums[i]
                solve(i+1,result)
                nums[i],nums[j] = nums[j],nums[i]
        solve(0,result)
        return result