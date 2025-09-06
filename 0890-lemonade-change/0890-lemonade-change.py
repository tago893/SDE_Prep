class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        amount_in_5 = 0
        amount_in_10 = 0

        for bill in bills:
            if bill == 5:
                amount_in_5+=1
            if bill == 10:
                amount_in_5-=1
                amount_in_10+=1
                if amount_in_5 < 0:
                    return False
            elif bill == 20:
                if amount_in_10>0:
                    amount_in_10-=1
                    amount_in_5-=1
                    if amount_in_5 < 0:
                        return False
                else:
                    if amount_in_5*5 >=15:
                        amount_in_5-=3
                    else:
                        return False

                

                    
        
        return True
