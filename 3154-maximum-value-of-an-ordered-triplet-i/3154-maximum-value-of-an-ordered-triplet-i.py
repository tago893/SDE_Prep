class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxElement = 0
        maxDiff = 0
        largest = 0
        for i in range(0,len(nums)):
            largest = max(largest, maxDiff*nums[i])
            maxDiff = max(maxDiff, maxElement - nums[i])
            maxElement = max(maxElement,nums[i])
        
        
        return largest