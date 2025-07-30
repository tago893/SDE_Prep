from collections import Counter
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            arr_char = [0]*26
            for ch in s:
                arr_char[ord(ch) - ord('a')]+=1
                if arr_char[ord(ch) - ord('a')] > 1:
                    return True
            return False
        else:
            index = []
            for i in range(0,len(s)):
                if s[i] != goal[i]:
                    index.append(i)
            
            if len(index) == 2:
                s_list = list(s)
                s_list[index[0]],s_list[index[1]] = s_list[index[1]],s_list[index[0]]  
                s = ''.join(s_list)
                return s == goal
            return False