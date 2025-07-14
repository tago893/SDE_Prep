class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # A string is not valid if the close bracket doesn't have its associated open bracket
        result = []
        
        def solve(curr_str,no_of_opens,no_of_closes):
            
            if len(curr_str) == 2*n:
                result.append(curr_str[:])
                return
            
            # open
            if no_of_opens<n:
                solve(curr_str + "(",no_of_opens+1,no_of_closes)
                
            #close
            if no_of_closes < no_of_opens:
                
                solve(curr_str + ")",no_of_opens,no_of_closes+1)

            
        solve("",0,0)
        
        return result