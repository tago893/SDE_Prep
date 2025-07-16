class Solution:
    def check(self, nums: List[int]) -> bool:
        def find_minimum_index(nums: List[int]) -> int:
            left, right = 0, len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > nums[right]:  # Rotation point is in the right half
                    left = mid + 1
                elif nums[mid] < nums[right]:  # Rotation point is in the left half
                    right = mid
                else:  # Handle duplicates by moving right inward
                    if nums[right - 1] > nums[right]:
                        left = right
                        break
                    right -= 1
            return left

        pivot = find_minimum_index(nums)
        nums = nums[pivot:] + nums[:pivot]  # Rotate back to check sorted order
        
        # Check if the rotated array is sorted
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return False
        return True