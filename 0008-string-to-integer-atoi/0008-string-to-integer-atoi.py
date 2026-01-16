class Solution:
    def myAtoi(self, s: str) -> int:
        max_int = 2**31 - 1
        min_int = -2**31
        i = 0
        while i<len(s) and s[i] == " ":
            i+=1
        if i == len(s):
            return 0
        sign = 1
        if s[i] == "+" or s[i] == "-":
            if s[i] == "-":
                sign = -1
            i+=1
        num = 0
        while i<len(s):
            if s[i] not in "0123456789":
                break
            digit = int(s[i])
            num = 10*num + digit
            i+=1
        if num*sign > max_int:
            return max_int
        elif num*sign < min_int:
            return min_int
        else:
            return num*sign        
