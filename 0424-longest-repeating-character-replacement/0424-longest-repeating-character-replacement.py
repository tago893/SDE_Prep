class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = defaultdict(int)
        i = 0
        j = 0
        mx = 0
        charcters = set(s)
        while j < len(s):
            res[s[j]]+=1
            while (j-i+1) - max(res.values()) >k:
                res[s[i]] -=1
                i+=1
            mx = max(mx,j-i+1)
            j+=1
            
        return mx
        