class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def getSorted(n):
            n = str(n)
            n = sorted(n)
            return n
        
        given_string = sorted(str(n))

        for i in range(0,30):
            sorted_string = getSorted(2**i) 
            print([given_string,sorted_string])
            if sorted_string == given_string:
                return True
        return False