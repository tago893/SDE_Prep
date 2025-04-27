class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Can be solved through Counter in python just write return Counter(s) == Counter(t)
        if len(s)!=len(t):
            return False
        count  = [0]*26
        for i in range(len(s)):
            count[ord(s[i])-ord('a')] += 1
        for i in range(len(t)):
            if count[ord(t[i])-ord('a')] != 0:
                count[ord(t[i])-ord('a')] -=1
            else:
                count[ord(t[i])-ord('a')]+=1
        
        for val in count:
            if val!=0:
                return False
                break
        return True
        
        