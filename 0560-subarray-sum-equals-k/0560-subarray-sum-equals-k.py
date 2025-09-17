class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0:1}
        count = 0
        sum = 0
        for i in range(0,len(nums)):
            sum+=nums[i]

            if sum-k in seen:
                count+=seen[sum-k]
            seen[sum] = seen.get(sum,0)+1
            
        return count
                