class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        r = n-1
        record = 0
        
        while l<r:
            mid = l + (r-l)//2

            if nums[mid] == nums[mid+1]:
                if (r-mid)%2==0:
                    l=mid+2
                else:
                    r = mid-1
            else:
                if (r-mid)%2==0:
                    r = mid
                else:
                    l = mid+1 
        return nums[r]



                