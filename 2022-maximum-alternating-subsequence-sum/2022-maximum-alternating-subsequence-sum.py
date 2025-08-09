class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        memo = collections.defaultdict(int)
        max_sum = 0
        
        def solve(i,isEven):
            if i>=n:
                return 0
            if (i,isEven) in memo:
                return memo[(i,isEven)]
            skip = solve(i+1,isEven)
            val = nums[i]
            if isEven == False:
                val = -val
            take = solve(i+1,not isEven) + val
            memo[(i,isEven)] = max(take,skip)
            return memo[(i,isEven)]
        
        return solve(0,True)