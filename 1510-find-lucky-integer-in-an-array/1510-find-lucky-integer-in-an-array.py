from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        frequency = Counter(arr)
        lucky_integer = -1
        for num,value in frequency.items():
            if num == value:
                if num > lucky_integer:
                    lucky_integer = num
        return lucky_integer
