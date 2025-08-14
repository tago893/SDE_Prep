class Solution:
    def largestGoodInteger(self, num: str) -> str:
        i,j = 0,0
        cur = ""
        best = -1
        while j<len(num):
            cur += num[j]
            if cur != num[i]*(j-i+1):
                while cur != num[i]*(j-i+1):
                    cur = cur[1:]
                    i+=1
            if len(cur) == 3:
                best = max(best,int(num[i]))
                
                

            j+=1
        if best == -1:
            return ""
        return str(best)*3