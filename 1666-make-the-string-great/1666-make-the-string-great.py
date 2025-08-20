class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        n = len(s)
        for i in range(0,n):
            if stack and abs(ord(s[i])-ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)
        