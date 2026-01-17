class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # Filter strings that have unique characters
        valid = [s for s in arr if len(s) == len(set(s))]
        
        def hasCommon(s1, s2):
            seen = set(s1)
            for ch in s2:
                if ch in seen:
                    return True
            return False
        
        def solve(index, temp):
            # Base case: reached end of valid array
            if index == len(valid):
                return len(temp)
            
            # Try excluding current string
            exclude = solve(index + 1, temp)
            
            # Try including current string if no common characters
            include = 0
            if not hasCommon(temp, valid[index]):
                include = solve(index + 1, temp + valid[index])
            
            return max(include, exclude)
        
        return solve(0, "")