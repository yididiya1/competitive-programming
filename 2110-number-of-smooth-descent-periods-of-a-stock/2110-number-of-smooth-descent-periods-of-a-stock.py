class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        
        
        result = prices.copy()
        result[-1] = 0
        
        
        for i in range(len(prices)-2,-1,-1):
            check = prices[i] - prices[i+1] == 1 
            result[i] = result[i+1] + 1 if check else 0 
        
        
        return sum(result) + len(prices)
            
        
        
        
        