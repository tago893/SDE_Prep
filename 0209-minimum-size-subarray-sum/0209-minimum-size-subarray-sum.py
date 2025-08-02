class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i,j = 0,0
        n = len(nums)
        min_length = float("inf")
        current_sum = 0
        while j<n and i<n:
            current_sum += nums[j]
            if current_sum >= target:
                while current_sum>=target:
                    current_sum -= nums[i] 
                    min_length = min(min_length,j-i+1)
                    i+=1
                    
            j+=1
        
        return min_length if min_length != float("inf") else 0
