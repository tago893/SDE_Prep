class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def find_common(a,b):
            res = ""
            i = 0
            n = len(b)
            while i<n:
                if a[i] == b[i]:
                    res+=b[i]
                else:
                    break
                i+=1
            
            return res
        min_string = strs[0]
        
        for string in strs:
            if len(min_string)>len(string):
                min_string = string
        res = min_string
        for string in strs:
            common_string = ""
            if string == min_string:
                continue
            else:
                common_string = find_common(string,min_string)
                if len(common_string)<len(res):
                    res = common_string
        return res

