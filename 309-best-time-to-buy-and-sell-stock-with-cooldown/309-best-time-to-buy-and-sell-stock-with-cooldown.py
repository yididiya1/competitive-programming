class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        
        def dp(index,isBuy):
            if index >= len(prices):
                return 0
            
            if (index,isBuy) in memo:
                return memo[(index,isBuy)]
            
            if isBuy:
                profit = dp(index+1, not isBuy) - prices[index]
                cooldown = dp(index+1,isBuy)
                memo[(index,isBuy)] = max(cooldown,profit)
            else:
                profit = dp(index+2,not isBuy) + prices[index]
                cooldown = dp(index+1,isBuy)
                memo[(index,isBuy)] = max(cooldown,profit)
                
            return memo[(index,isBuy)]
        
        return dp(0,True)
        
        
        
        
        