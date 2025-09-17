class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        n = len(prices)
        max_profit = 0
        while r<n:
            
            if prices[l]>=0 and prices[l]<prices[r]:
                max_profit = max(max_profit,prices[r]-prices[l])
            else:
                l=r
            r+=1
        return max_profit