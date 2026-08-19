class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memory = {}
        return self.dfs(0,True,prices,memory)

        # [1,2,3]
        # buy sell buy
        # hold hold buy
        

    def dfs(self,index,canBuy, prices,memory):
        if index >= len(prices):
            return 0
        if (index, canBuy) in memory:
            return memory[(index, canBuy)]
        if canBuy:
            buying = -prices[index] + self.dfs(index+1,False,prices,memory)
            holding = self.dfs(index+1,True,prices,memory)
            memory[index,canBuy] = max(buying,holding)
        else:
            selling = prices[index] + self.dfs(index+1,True,prices,memory)
            holding = self.dfs(index+1,False,prices,memory)
            memory[index,canBuy] = max(selling,holding)
        return memory[index,canBuy]
    

        