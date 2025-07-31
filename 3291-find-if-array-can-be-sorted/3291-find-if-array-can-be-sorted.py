from collections import defaultdict
from typing import List

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        # First check if already sorted
        is_sorted = True
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                is_sorted = False
                break
        
        if is_sorted:
            return True
        
        # Group consecutive numbers with same bit count into segments
        segments = []
        current_segment = [nums[0]]
        current_bit_count = bin(nums[0]).count('1')
        
        for i in range(1, len(nums)):
            bit_count = bin(nums[i]).count('1')
            if bit_count == current_bit_count:
                current_segment.append(nums[i])
            else:
                segments.append(current_segment)
                current_segment = [nums[i]]
                current_bit_count = bit_count
        
        segments.append(current_segment)  # Don't forget the last segment
        
        # Sort each segment
        for segment in segments:
            segment.sort()
        
        # Check if segments can form a sorted array
        for i in range(1, len(segments)):
            if min(segments[i]) < max(segments[i-1]):
                return False
        
        return True
