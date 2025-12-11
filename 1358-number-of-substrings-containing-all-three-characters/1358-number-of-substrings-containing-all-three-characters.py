class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq = [0, 0, 0]

        # Initialize left pointer and result
        left = 0
        res = 0

        # Traverse the string with right pointer
        for right in range(len(s)):
            # Increment frequency of current character
            freq[ord(s[right]) - ord('a')] += 1

            # Shrink the window while all characters are present
            while freq[0] > 0 and freq[1] > 0 and freq[2] > 0:
                # Add valid substrings from current right to end
                res += len(s) - right

                # Move left pointer and update frequency
                freq[ord(s[left]) - ord('a')] -= 1
                left += 1

        return res