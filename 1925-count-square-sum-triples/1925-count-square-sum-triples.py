class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for i in range(1,n):
            for j in range(i+1,n+1):
                k = i*i + j*j
                r = int(math.sqrt(k))
                if r<=n and r*r == k:
                    count+=2
        return count
                