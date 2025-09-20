from typing import List

class Solution:
    """
    Counts the number of reverse pairs (i < j, nums[i] > 2*nums[j]) in a list using modified merge sort.
    Efficiently counts pairs before merging sorted halves to avoid missing cases.
    """
    def reversePairs(self, nums: List[int]) -> int:
        def mergeSortAndCount(arr: List[int], low: int, high: int) -> int:
            if low >= high:  # Base case: 1 element
                return 0
            mid = (low + high) // 2
            count = mergeSortAndCount(arr, low, mid)      # Sort left
            count += mergeSortAndCount(arr, mid + 1, high)  # Sort right

            # Count valid pairs (i in left, j in right)
            j = mid + 1
            for i in range(low, mid + 1):
                while j <= high and arr[i] > 2 * arr[j]:
                    j += 1
                count += j - (mid + 1)

            # Merge left and right
            temp = []
            left, right = low, mid + 1
            while left <= mid and right <= high:
                if arr[left] <= arr[right]:
                    temp.append(arr[left])  # Left smaller, keep sorted order
                    left += 1
                else:
                    temp.append(arr[right])
                    right += 1
            while left <= mid:
                temp.append(arr[left])
                left += 1
            while right <= high:
                temp.append(arr[right])
                right += 1
            # Write merged result back
            for i in range(low, high + 1):
                arr[i] = temp[i - low]
            return count

        # Start recursive process
        return mergeSortAndCount(nums, 0, len(nums) - 1)
