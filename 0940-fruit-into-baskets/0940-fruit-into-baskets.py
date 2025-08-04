from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i,j = 0,0
        n = len(fruits)
        count = defaultdict(int)
        max_number = 0

        while j<n:
            count[fruits[j]]+=1
            while len(count)>=3:
                count[fruits[i]]-=1
                if count[fruits[i]] == 0:
                    del count[fruits[i]]
                i+=1
            
            max_number = max(max_number,j-i+1)
            j+=1
        
        return max_number


        
