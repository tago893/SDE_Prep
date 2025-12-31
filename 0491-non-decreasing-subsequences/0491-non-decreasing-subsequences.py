class Solution:
    def findSubsequences(self,nums):
        result = []
        path = []

        def backtrack(start):
            # If we have at least 2 elements, add a copy of current path
            if len(path) >= 2:
                result.append(path[:])  # Make a copy
            
            # Use a set to avoid starting with the same value twice at this level
            used = set()
            
            for i in range(start, len(nums)):
                if nums[i] in used:
                    continue  # Skip duplicates at this recursion level
                
                # Maintain non-decreasing order
                if path and nums[i] < path[-1]:
                    continue  # Not valid — breaks non-decreasing
                
                # Include current number
                path.append(nums[i])
                used.add(nums[i])  # Mark this value as used at this level
                
                # Recurse from next index
                backtrack(i + 1)
                
                # Backtrack
                path.pop()

        backtrack(0)
        return result