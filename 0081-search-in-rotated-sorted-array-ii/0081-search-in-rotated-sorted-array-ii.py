class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l<=r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return True
            while l < mid and nums[l] == nums[mid]:
                l += 1
            while r > mid and nums[r] == nums[mid]:
                r -= 1
            
            # rotated
            if nums[mid] >= nums[l]:
                if target<nums[mid] and target>=nums[l]:
                    r = mid-1
                else:
                    l = mid+1
            #sorted
            else:
                if target > nums[mid] and target<=nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
