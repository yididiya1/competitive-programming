class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        mapp = {'2':['a','b','c'] , '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l']
               , '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']
               }
        output = []
        
        if digits == "":
            return []
        
        digits = list(digits)
        
        
        
        def rec(index):
            if index == len(digits):
                return [""]
            
            x = []
            
            for char in mapp[digits[index]]:
                for child in rec(index+1):
                    x.append(char+child)
                    
            return x
        
        output = rec(0)
        return output
        