class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        power_arr = []
        i = 1
        while n>0:
            if n%2 == 1:
                power_arr.append(i)
            n//=2
            i*=2

        mod = 10**9  + 7
        ans = []     
        for i,j in queries:
            curr = 1
            for k in range(i,j+1):
                curr=(curr*power_arr[k])%mod
            ans.append(curr)
        return ans

