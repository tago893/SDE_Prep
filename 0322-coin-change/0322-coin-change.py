class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        ways = []
        total = 0
        memo = [[-1 for _ in range(amount)] for _ in range(len(coins))]
        min_number_of_coins = float("inf")
        n = len(coins)
        def solve(i,amount,total):
            # nonlocal min_number_of_coins
            # if total == amount:
            #     # min_number_of_coins = min(min_number_of_coins,len(way))
            #     # ways.append(way[:])
            if i>=n or total>=amount:
                if total==amount:
                    return 0
                return float("inf")
            if memo[i][total] != -1:
                return memo[i][total]
            res=-1    
            if coins[i]>amount:
                exclude = 0+solve(i+1,amount,total)
                memo[i][total]=res = exclude 
            # way.append(coins[i])
            include = 1+solve(i,amount,total+coins[i])
            # way.pop()
            exclude = 0+solve(i+1,amount,total)
            memo[i][total]=res = min(include,exclude)
            return memo[i][total]
        min_number_of_coins = solve(0,amount,total)
        if min_number_of_coins == float("inf"):
            return -1
        return min_number_of_coins 