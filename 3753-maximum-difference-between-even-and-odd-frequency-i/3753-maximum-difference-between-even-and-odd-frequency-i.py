from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        frequency = Counter(s)
        even_frequency = float("inf")
        odd_frequency = float("-inf")
        print(frequency.values())
        for value in frequency.values():
            if value % 2 == 0:
                even_frequency = min(value,even_frequency)
            else:
                odd_frequency = max(value,odd_frequency) 
        
        return odd_frequency - even_frequency