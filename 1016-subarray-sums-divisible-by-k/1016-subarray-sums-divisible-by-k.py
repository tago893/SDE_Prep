class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        seen = {0:1}
        sum = 0
        result = 0
        for i in range(len(nums)):
            sum+=nums[i]
            rem = sum%k
            if rem<0:
                rem+=k
            if rem in seen:
                result+=seen[rem]
                seen[rem]+=1
            else:
                seen[rem]=1
        
        return result