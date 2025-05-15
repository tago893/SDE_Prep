class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        n = len(nums)
        ans = [1]*len(nums)

        for i in range(0,len(nums)):
            ans[i]=ans[i]*prefix
            prefix = prefix*nums[i]

        for i in range(len(nums)-1,-1,-1):
            ans[i]=ans[i]*suffix
            suffix = suffix*nums[i]

        return ans
