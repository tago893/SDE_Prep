class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        if s[0] == "*":
            s = s[1:]
        for i in range(0,len(s)):
            if stack and s[i] == "*":
                stack.pop()
            else:
                stack.append(s[i])
        
        result = []
        while stack:
            result.append(stack.pop())
        return ''.join(reversed(result))