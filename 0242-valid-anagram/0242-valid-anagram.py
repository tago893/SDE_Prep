class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Can be solved through Counter in python just write return Counter(s) == Counter(t)
        hash_map_s = {}
        hash_map_t = {}
        if len(s)!=len(t):
            return False

        for i in s:
            if i in hash_map_s:
                hash_map_s[i]+=1
            else:
                hash_map_s[i] = 1
        
        for i in t:
            if i in hash_map_t:
                hash_map_t[i]+=1
            else:
                hash_map_t[i]= 1
        
        return hash_map_s == hash_map_t
        
        