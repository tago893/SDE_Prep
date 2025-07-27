class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        hills = 0
        valleys = 0
        left = 0
        n = len(nums)
        for i in range(1,n-1):
            if nums[i] == nums[i+1]:
                continue
            else:
                if nums[i] > nums[i+1] and nums[i] > nums[left]:
                    hills+=1
                elif nums[i] < nums[i+1] and nums[i] < nums[left]:
                    valleys+=1
                left = i
        return hills + valleys