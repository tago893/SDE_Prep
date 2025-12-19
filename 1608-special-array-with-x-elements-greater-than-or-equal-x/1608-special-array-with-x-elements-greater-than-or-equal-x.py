class Solution:
    def feasible(self,nums,x):
            count = 0
            for num in nums:
                if num>=x:
                    count+=1
            
            return count
    def specialArray(self, nums: List[int]) -> int:
        n = max(nums)
        l = 1
        r = n
        
        while l<=r:
            mid = l + (r-l)//2
            count = self.feasible(nums,mid)
            if count>mid:
                l = mid+1
            elif count == mid:
                return mid
            else:
                r = mid-1
        return -1   