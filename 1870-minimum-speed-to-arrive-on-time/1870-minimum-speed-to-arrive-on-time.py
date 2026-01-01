class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        def feasible(speed):
            i=0 
            time = 0
            while i<n-1:
                time += math.ceil(dist[i]/speed)
                if time>hour:
                    return False
                i+=1
            
            if time + dist[i]/speed > hour:
                return False
            return True

        l = 1
        r = 10**7
        ans = -1
        while l<=r:
            mid = l + (r-l)//2
            if feasible(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid+1
        return ans 
            
