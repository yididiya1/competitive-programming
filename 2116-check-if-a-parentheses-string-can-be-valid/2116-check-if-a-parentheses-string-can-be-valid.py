class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        
        if len(s)%2 != 0:
            return False
        
        def canBeBalanced(s,locked,isOpening):
            s = s if isOpening else s[::-1]
            locked = locked if isOpening else locked[::-1]
            checkingParentheses = '(' if isOpening else ')' 
            
            changables  = 0
            need_balancing = 0
            
            for i in range(len(s)):
                if locked[i] == '1':
                    if s[i] == checkingParentheses:
                        need_balancing += 1
                    else:
                        need_balancing -= 1           
                else:
                    changables += 1
                if changables+need_balancing < 0:
                    return False
                
            return need_balancing <= changables
            
        return canBeBalanced(s,locked,True) and canBeBalanced(s,locked,False)