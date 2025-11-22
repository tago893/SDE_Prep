class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        curr_string = ""
        currentNum = 0
        for ch in s:
            if ch == "[":
                stack.append(curr_string)
                stack.append(currentNum)
                curr_string = ''
                currentNum = 0
            elif ch == "]":
                num = stack.pop()
                prv_string = stack.pop()
                curr_string = prv_string+num*curr_string
            elif ch.isdigit():
                currentNum = currentNum*10+int(ch)
            else:
                curr_string += ch
        return curr_string 
