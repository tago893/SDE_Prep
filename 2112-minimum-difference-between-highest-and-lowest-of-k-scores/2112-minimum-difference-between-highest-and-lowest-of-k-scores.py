class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        j = 0
        i = 0
        diff = float("inf")
        while j<len(nums): 
            if j-i+1 == k:
                diff = min(diff,nums[j]-nums[i])
                i+=1
            j+=1
        return diff