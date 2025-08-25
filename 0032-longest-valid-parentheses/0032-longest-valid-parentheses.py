class Solution:
    def longestValidParentheses(self, s: str) -> int:
        length = 0
        max_length = 0
        stack = [-1]
        n = len(s)
        for i in range(n):
            if s[i] == ')':
                stack.pop()
                if len(stack)==0:
                    stack.append(i)
                else:
                    max_length = max(max_length,i-stack[-1])
            else:
                stack.append(i)
        return max_length