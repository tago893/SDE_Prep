class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_string = strs[0]
        for string in strs:
            if len(min_string)>len(string):
                min_string = string
        res = min_string
        i=0
        
        while i<len(res):
            for s in strs:
                if s[i]!=strs[0][i]:
                    return s[:i]
            i+=1
        return res

