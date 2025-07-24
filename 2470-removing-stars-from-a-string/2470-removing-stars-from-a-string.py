class Solution:
    def removeStars(self, s: str) -> str:
        result = []
        if s[0] == "*":
            s = s[1:]
        for i in range(0,len(s)):
            if s[i] == "*":
                result.pop()
            else:
                result.append(s[i])
        
        return ''.join(result)