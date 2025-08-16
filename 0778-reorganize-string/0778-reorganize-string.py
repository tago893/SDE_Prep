from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_count = max(count.values())
        
        # If the most frequent character is too frequent, it's impossible
        if max_count > (len(s) + 1) // 2:
            return ""
        
        # Sort characters by frequency
        sorted_chars = sorted(count.items(), key=lambda x: -x[1])
        
        res = [""] * len(s)
        idx = 0
        
        # Place the most frequent characters first at even indices
        for ch, freq in sorted_chars:
            for _ in range(freq):
                res[idx] = ch
                idx += 2
                if idx >= len(s):
                    idx = 1  # switch to odd indices
        
        return "".join(res)
