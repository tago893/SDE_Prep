class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def solve(nums,goal):
            i,j = 0,0
            if goal<0:
                return 0
            sum = 0
            res = 0
            while j<len(nums):
                sum+=nums[j]
                while sum>goal:
                    sum-=nums[i]
                    i+=1
                res+=(j-i+1)
                j+=1
            
            return res
        return solve(nums,goal) - solve(nums,goal-1)