class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_map = {}
        for i,ch in enumerate(order):
            char_map[ch] = i
        res = True
        
        def check(a,b):
            n1 = len(a)
            n2 = len(b)
            i = 0
            j = 0
            while i<min(n1,n2):
                ch1 = a[i]
                ch2 = b[i]
                if ch1!=ch2:
                    if char_map[ch1]>char_map[ch2]:
                        return True
                    else:
                        return False
                i+=1
                j+=1
            if n1>n2:
                return True
            return False
            

        for i in range(0,len(words)-1):
            word_a = words[i]
            word_b = words[i+1]
            if check(word_a,word_b):
                res = False
                break
        return res
            