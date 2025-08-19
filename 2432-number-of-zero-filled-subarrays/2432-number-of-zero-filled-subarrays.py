class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        nums.append(1)
        count_zero = 0
        ans = 0
        n = len(nums)
        for i in range(0,n):
            if nums[i] == 0:
                count_zero+=1 
            else:
                count_zero=0
            ans+=count_zero
        return(ans)