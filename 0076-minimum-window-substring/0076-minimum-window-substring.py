class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        s_count = defaultdict(int)
        i = 0
        have,need = 0,len(t_count)
        j = 0
        min_length = float("inf")
        min_string = ""
        while j<len(s):
            ch = s[j]
            if ch in t_count.keys():
                s_count[ch]+=1
                if s_count[ch] == t_count[ch]:
                    have+=1
            while have == need:
                if j-i+1<min_length:
                    min_length = j-i+1
                    min_string = s[i:j+1]
                if s[i] in t_count:
                    s_count[s[i]] -= 1
                    if t_count[s[i]] > s_count[s[i]]:
                        have-=1
                i+=1
            j+=1
        return min_string