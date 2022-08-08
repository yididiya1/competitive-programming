class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        @cache
        def dp(index):
            if index > len(stoneValue)-1:
                return 0
             
            
                
            take_one = float('-inf')
            take_two = float('-inf')
            take_three = float('-inf')
            
            if index < len(stoneValue):
                take_one = stoneValue[index] - dp(index+1)
            if index+1 < len(stoneValue):
                take_two = stoneValue[index] + stoneValue[index+1]  - dp(index+2)
            if index+2 < len(stoneValue):
                take_three = stoneValue[index] + stoneValue[index+1] + stoneValue[index+2] - dp(index+3)
                
            
            # print(index,take_one,take_two,take_three)
            return max(take_one,take_two,take_three)
        
        x = dp(0)
        # print(x)
        if x > 0:return "Alice"
        elif x == 0 : return "Tie"
        else: return "Bob"
        