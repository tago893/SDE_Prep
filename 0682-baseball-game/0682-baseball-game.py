class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = 0
        stack = []
        top = -1
        for c in operations:
            if c == "D":
                value = stack[top]
                stack.append(value*2)
                result+=(value*2)
                top+=1
            elif c == "C":
                result -= stack[top]
                stack.pop()
                top-=1

            elif c == "+":
                value = stack[top] + stack[top-1]
                stack.append(value)
                result+=value
                top+=1
            else:
                stack.append(int(c))
                result += int(c) 
                top+=1
        return result