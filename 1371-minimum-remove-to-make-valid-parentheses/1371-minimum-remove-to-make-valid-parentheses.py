class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove = set()
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()     # matched
                else:
                    remove.add(i)   # unmatched ')'
        # remaining '(' are unmatched
        remove.update(stack)

        result = [c for i, c in enumerate(s) if i not in remove]
        return "".join(result)
