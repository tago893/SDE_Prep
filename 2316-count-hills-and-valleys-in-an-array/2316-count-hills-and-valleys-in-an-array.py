class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        hills = 0
        valleys = 0
        n = len(nums)
        for i in range(1,n-1):
            if nums[i] == nums[i-1]:
                continue
            right = i+1
            left = i-1
            while right<n and nums[right] == nums[i]:
                right+=1
            print(right)
            if right<n:
                if nums[i] > nums[right] and nums[i] > nums[left]:
                    hills+=1
                elif nums[i] < nums[right] and nums[i] < nums[left]:
                    valleys+=1
        return hills + valleys