class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0 
        r = n-1
        while l<r:
            mid = l + (r-l)//2
            if mid%2  == 1:
                mid-=1
            if nums[mid]!=nums[mid+1]:
                r = mid
            else:
                l = mid+2

        return nums[l]