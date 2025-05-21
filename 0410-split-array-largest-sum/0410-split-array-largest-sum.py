class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        
        def check(sum_value):
            total = 0
            K=1
            for num in nums:
                total+=num
                if total>sum_value:
                    total = num
                    K+=1
                    if K>k:
                        return False
            return True
            
        l,r = max(nums),sum(nums)
        while l<r:
            mid = l+(r-l)//2
            if check(mid):
                r = mid
            else:
                l=mid+1 

        
        return l
        
        
                