class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        left_product = 1
        right_product = 1
        n=len(nums)
        max_product = float("-inf")
        for i in range(0,len(nums)):
            if left_product==0:
                left_product =1
            elif right_product==0:
                right_product =1
            #prefix product    
            left_product = left_product*nums[i]
            #suffix product
            right_product = right_product*nums[n-1-i]
            
            max_product = max(left_product,right_product,max_product)
        return max_product
