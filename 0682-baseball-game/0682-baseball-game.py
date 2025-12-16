class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = 0
        stack = []
        for c in operations:
            if c == "D":
                value = stack[-1]
                stack.append(value*2)
                result+=(value*2)
            elif c == "C":
                result -= stack[-1]
                stack.pop()

            elif c == "+":
                value = stack[-1] + stack[-2]
                stack.append(value)
                result+=value
            else:
                stack.append(int(c))
                result += int(c) 
        return result