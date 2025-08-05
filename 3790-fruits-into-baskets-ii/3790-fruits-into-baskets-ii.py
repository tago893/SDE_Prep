class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        for i in range(0,n):
            for j in range(0,n):
                if baskets[j] >= fruits[i]:
                    baskets[j] = -1
                    break
        count = 0
        for i in range(0,n):
            if baskets[i] != -1:
                count+=1
        return count