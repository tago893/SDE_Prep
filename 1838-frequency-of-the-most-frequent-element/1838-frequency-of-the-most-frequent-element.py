class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_freq = float("-inf")
        curr_sum = 0
        i,j = 0,0
        while j<len(nums):
            curr_sum = curr_sum + nums[j]
            while(nums[j]*(j-i+1) - curr_sum)>k:
                curr_sum -= nums[i]
                i = i+1
            max_freq = max(max_freq,j-i+1)
            j+=1
        return max_freq