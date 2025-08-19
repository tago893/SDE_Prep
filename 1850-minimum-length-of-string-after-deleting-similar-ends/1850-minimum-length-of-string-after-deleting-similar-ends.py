class Solution:
    def minimumLength(self, s: str) -> int:
        l = 0
        n = len(s) 
        r = n-1
        k = n
        while l<r and s[l]==s[r]:
            ch = s[l]
            while l<r and s[l] == ch:
                l+=1
            while r>=l and s[r] == ch:
                r-=1
        
 
        return r-l+1