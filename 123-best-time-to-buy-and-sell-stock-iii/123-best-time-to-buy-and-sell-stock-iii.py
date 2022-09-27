class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left_min,left_profit = prices[0],[0]
        right_max = prices[-1]
        right_profit = [0] * (len(prices) +1)
        
        for i in range(1,len(prices)):
            left_profit.append(max(left_profit[i-1],prices[i]-left_min))
            left_min = min(left_min,prices[i])
            
        for i in range(len(prices)-2,-1,-1):
            right_profit[i] = max(right_profit[i+1],right_max - prices[i])
            right_max = max(right_max,prices[i])
            
        
        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit,left_profit[i]+right_profit[i+1])
            
        return max_profit