class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.lstrip()
        s = s.rstrip()
        length = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == " ":
                break
            else:
                length+=1
        return length