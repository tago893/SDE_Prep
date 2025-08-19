class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count_zero = 0
        ans = 0
        n = len(nums)
        for i in range(0,n):
            if nums[i] == 0:
                count_zero+=1 
            else:
                ans += count_zero*(count_zero+1)//2
                count_zero=0
        ans+=count_zero*(count_zero+1)//2
        return(ans)