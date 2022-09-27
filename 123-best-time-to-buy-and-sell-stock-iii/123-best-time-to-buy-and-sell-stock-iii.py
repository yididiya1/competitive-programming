class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @cache
        def dp(index,canBuy,left):
            if index >= len(prices):
                return 0
            
            
            buy,not_buy = 0,0
            sell,not_sell = 0,0
            
            if canBuy and left > 0:
                buy = -prices[index] +  dp(index+1,False,left)
                not_buy = dp(index+1,True,left)
            
            elif not canBuy:
                sell = prices[index] + dp(index+1,True,left-1)
                not_sell = dp(index+1,False,left)
            
            return max(buy,not_buy,sell,not_sell)
        
        return dp(0,True,2)