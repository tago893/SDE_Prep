class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(capacity):
            total = 0
            D = 1
            for weight in weights:
                total+=weight
                if total>capacity:
                    total = weight
                    D+=1
                    if D>days:
                        return False
            return True
        l,r=max(weights),sum(weights)
        while l<r:
            mid = l+(r-l)//2
            if feasible(mid):
                r=mid
            else:
                l=mid+1
        
        return l