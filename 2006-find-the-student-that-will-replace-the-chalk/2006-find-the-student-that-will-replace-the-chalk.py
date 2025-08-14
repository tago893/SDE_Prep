class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        if n==1:
            return 0
        sum_chalk = 0
        for i in range(0,n):
            sum_chalk+=chalk[i]
            if sum_chalk > k:
                break
        k = k%sum_chalk
        for i in range(0,n):
            
            if chalk[i]>k:
                return i
            k = k - chalk[i]
        
        return i

