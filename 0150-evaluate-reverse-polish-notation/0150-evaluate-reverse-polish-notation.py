class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(0,len(tokens)):
            if tokens[i] == "+":
                stack.append(stack.pop() + stack.pop())
            elif tokens[i] == "*":
                stack.append(stack.pop()*stack.pop())
            elif tokens[i] == "-":
                a,b = stack.pop(),stack.pop()
                stack.append(b-a)
    
            elif tokens[i] == "/":
                curr_div = stack.pop()
                value = stack.pop()
                curr_div=int(value/curr_div)
                    
                stack.append(curr_div)
            else:
                stack.append(int(tokens[i])) 
        result = stack.pop()
        return result