class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        def time_taken(rate):
            hour = 0
            for pile in piles:
                hour += math.ceil(pile/rate)
                if hour>h:
                    return False
            
            return True

        while l<r:
            mid = l + (r-l)//2
            if time_taken(mid):
                r = mid
            else:
                l=mid+1
        return l
