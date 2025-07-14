class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k = len(needle)
        if len(haystack)<len(needle):
            return -1
        def compare(str1,str2):
            print([str1,str2])
            if len(str1) < len(str2):
                return False
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    return False
            return True
        for i in range(len(haystack)):
            if compare(haystack[i:i+k],needle):
                return i
        
        return -1 