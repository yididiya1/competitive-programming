class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        self.output = []
        
        def dfs(arr,open_left,close_left):
            if len(arr) == n*2:
                self.output.append("".join(arr))
                return
            
            
            if open_left > 0 and len(arr) < (n*2)-1 and close_left >= open_left:
                x = arr.copy()
                x.append('(')
                dfs(x,open_left-1,close_left)
            
            if close_left > 0 and len(arr) > 0:
                y = arr.copy()
                y.append(')')
                dfs(y,open_left,close_left-1)
                
                
        dfs([],n,n)
        return self.output
                    
        