from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        mx = 0
        res = defaultdict(int)
        
        for right in range(len(s)):
            while res[s[right]] > 0:
                res[s[left]] -= 1
                left += 1
            res[s[right]] += 1
            mx = max(mx, right - left + 1)
        
        return mx
