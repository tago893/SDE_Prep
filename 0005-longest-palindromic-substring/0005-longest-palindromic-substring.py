class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start, end = 0, 0  # track best palindrome window

        def expand_around_center(left, right):
            # expand while valid and characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # when loop ends, we’ve gone one step too far
            return left+1, right-1

        for i in range(len(s)):
            # odd length palindrome
            l1, r1 = expand_around_center(i, i)
            # even length palindrome
            l2, r2 = expand_around_center(i, i+1)

            # pick the longer one
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end+1]
