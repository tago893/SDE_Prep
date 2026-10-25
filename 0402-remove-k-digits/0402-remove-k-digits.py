class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        s = []
        if k == 0:
            return num
        for digit in num:
            while k>0 and s and s[-1]>digit:
                s.pop()
                k-=1
            s.append(digit)

        while k>0:
            s.pop()
            k-=1
        
        s=''.join(s)
        s = s.lstrip("0")
        return s if len(s)!=0 else '0'
