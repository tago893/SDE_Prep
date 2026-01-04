class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        # primality check video codestorywithmik one for conecpt understanding of sieve
        total = 0
        for x in nums:
            cnt = 0
            s = 0
            for fact in range(1,int(math.sqrt(x))+1):
                if x%fact == 0:
                    other = x//fact
                    if other == fact:
                        cnt+=1
                        s+=fact
                    else:
                        cnt+=2
                        s+=fact+other
                
                if cnt>4:
                    break
            if cnt == 4:
                total += s
        return total