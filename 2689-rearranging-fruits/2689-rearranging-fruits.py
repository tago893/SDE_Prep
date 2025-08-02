from collections import Counter
class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count = Counter(basket1)
        min_ele = min(basket1)
        for x in basket2:
            count[x] -= 1
            min_ele = min(min_ele,x)
        merge = []
        for k,v in count.items():
            if v%2 != 0:
                return -1
            merge.extend([k]*(abs(v)//2))
        
        if not merge:
            return 0
        merge.sort()
        return sum(min(2*min_ele,x) for x in merge[:len(merge)//2])