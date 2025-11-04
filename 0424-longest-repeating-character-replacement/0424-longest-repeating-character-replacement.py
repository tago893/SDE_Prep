class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = defaultdict(int)
        i = 0
        j = 0
        mx = 0
        while j<len(s):
            char_count[s[j]] += 1
            while (j-i+1) - max(char_count.values())>k:
                char_count[s[i]]-=1
                i+=1
            mx = max(mx,j-i+1)
            j+=1
        return mx
