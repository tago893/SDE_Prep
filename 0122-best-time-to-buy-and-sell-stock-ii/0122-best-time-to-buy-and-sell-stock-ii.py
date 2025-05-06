class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        l= 0 
        r = 1
        n = len(prices)
        while r<n:
            if prices[l]<prices[r]:
                profit=prices[r] - prices[l]
                max_profit = profit+max_profit
            l=r
            r+=1
        
        return max_profit
        