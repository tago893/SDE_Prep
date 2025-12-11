class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        goal = k
        for i in range(0,len(nums)):
            if nums[i]%2!=0:
                nums[i] = 1
            else:
                nums[i] = 0

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