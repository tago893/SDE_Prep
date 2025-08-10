class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans = 2**31 -1
        for i in range(0,len(nums)):
            if nums[i] == i:
                continue
            ans = ans & nums[i]
        
        if ans!=2**31 -1:
            return ans
        return 0