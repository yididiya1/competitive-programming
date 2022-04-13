class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
         
        @cache    
        def dp(index): 
            
            if index > len(questions) - 1:
                return 0
            
            points,idx = questions[index]
             
            solve = dp(index+(idx)+1)
            skip = dp(index+1)
            
            return max(points+solve,skip)
        
        return dp(0)
        
        
            
                
                
                
        
        