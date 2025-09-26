class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []

        # Traverse nums2 in reverse to build the map of next greater elements
        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop()
            next_greater[num] = stack[-1] if stack else -1
            stack.append(num)

        # Build result for nums1 using the map
        return [next_greater[num] for num in nums1]