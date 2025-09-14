class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        t = 1
        while True:
            val = num1-t*(num2)
            if val<=0:
                return -1
            no_of_bits = val.bit_count()
            if no_of_bits<=t<=val:
                return t
            t+=1
        

        
