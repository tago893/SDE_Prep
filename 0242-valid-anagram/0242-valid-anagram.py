class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_map = [0]*26
        if len(s) != len(t):
            return False
        
        for i in range(0,len(s)):
            char_map[ord(s[i])-ord('a')]+=1

        for i in range(0,len(t)):
            char_map[ord(t[i])-ord('a')]-=1

        for i in range(0,26):
            if char_map[i] <0:
                return False
        return True 