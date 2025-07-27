from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        seen = set()
        max_sum = 0
        max_negative = float('-inf')

        for num in nums:
            if num < 0:
                max_negative = max(max_negative, num)
            elif num not in seen:
                max_sum += num
                seen.add(num)
        return max_negative if max_sum == 0 and len(seen) == 0 else max_sum