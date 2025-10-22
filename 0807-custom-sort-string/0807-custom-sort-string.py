class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_freq = [0]*26
        res = []
        order_freq = [0]*26
        for ch in s:
            s_freq[ord(ch)-ord('a')]+=1
        for ch in order:
            order_freq[ord(ch)-ord('a')]+=1
            
        for ch in order:

            if s_freq[ord(ch)-ord('a')]>0 and order_freq[ord(ch)-ord('a')]>0:
                res.append(s_freq[ord(ch)-ord('a')]*ch)
                s_freq[ord(ch)-ord('a')]-= (1*s_freq[ord(ch)-ord('a')])
        for ch in s:
            if s_freq[ord(ch)-ord('a')]>0:
                res.append(s_freq[ord(ch)-ord('a')]*ch)
                s_freq[ord(ch)-ord('a')]-=(1*s_freq[ord(ch)-ord('a')])
        return ''.join(res)
                