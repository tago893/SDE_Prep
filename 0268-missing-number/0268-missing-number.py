class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0
        i = 0
        while i<len(nums):
            correct = nums[i]
            if nums[i]<len(nums) and nums[i]!=nums[correct]:
                nums[i],nums[correct] = nums[correct],nums[i]
            else:
                i+=1
        
        for i in range(0,len(nums)):
            if nums[i]!=i:
                return i
        
        return len(nums)