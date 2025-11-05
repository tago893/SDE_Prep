class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        sum_of_the_arrays = []
        def subarrays(nums):
            for i in range(0,len(nums)):
                sums=0
                for j in range(i,len(nums)):
                    sums+=nums[j]
                sum_of_the_arrays.append(sums)
            return sum_of_the_arrays
        
        subarrays(nums)
        l,r = min(sum_of_the_arrays),max(sum_of_the_arrays)
        
        def check(sum_value):
            K=1
            total = 0
            for num in nums:
                total+=num
                if total>sum_value:
                    K+=1
                    total=num
                    if K>k:
                        return False
                
            return True
        while l<r:
            mid = l+(r-l)//2
            if check(mid):
                r = mid
            else:
                l = mid+1
        return l
                