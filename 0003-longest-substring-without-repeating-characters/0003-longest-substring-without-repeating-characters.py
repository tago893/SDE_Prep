class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = defaultdict(int)
        i = 0
        j = 0
        mx = 0
        while j < len(s):
            res[s[j]]+=1
            
            if len(res) == j-i+1:
                mx = max(mx,j-i+1)
                j+=1
            elif len(res) < j-i+1:
                while len(res)<j-i+1:
                    res[s[i]]-=1
                    if res[s[i]] == 0:
                        res.pop(s[i])
                    i+=1
                j+=1
        
        return mx