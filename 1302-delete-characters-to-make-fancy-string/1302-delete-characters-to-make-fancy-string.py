class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) <=2:
            return s
        result = ""
        temp = s[0]
        result+=s[0]
        count = 1
        for i in range(1,len(s)):
            if temp == s[i]:
                count+=1
            else:
                temp =s[i]
                count = 1
            if count < 3:
                result+=s[i]
            
        return result
