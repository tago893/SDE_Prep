class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        min_prod = nums[0]
        result = nums[0]
        for i in range(1,len(nums)):
            if nums[i]<0:
                max_prod,min_prod = min_prod,max_prod
            max_prod = max(max_prod*(nums[i]),nums[i])
            min_prod = min(min_prod*(nums[i]),nums[i])
            result = max(result,max_prod)
        return result