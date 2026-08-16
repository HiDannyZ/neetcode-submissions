class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = 0 
        l = 0
        for r in range(1,len(prices)):
            price = prices[r]

            profit = prices[r] - prices[l]
            res = max(res,profit)
            
            if profit <= 0:
                l = r        
        return res