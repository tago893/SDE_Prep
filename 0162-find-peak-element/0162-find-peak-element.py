class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1
        while l < h:
            mid = l + (h - l) // 2
            if nums[mid] < nums[mid + 1]:
                # Peak is to the right
                l = mid + 1
            else:
                # Peak is at mid or to the left
                h = mid
        return l