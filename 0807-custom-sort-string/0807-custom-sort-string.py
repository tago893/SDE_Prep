class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_freq = Counter(s)
        res = []
        print(s_freq)
        for ch in order:
            if ch in s_freq:
                res.append(s_freq[ch]*ch)
                del s_freq[ch]
        print(s_freq)
        for ch,count in s_freq.items():
            res.append(count*ch)
        return ''.join(res)
                