class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        s_stack = []
        t_stack = []
        
        s_pointer = 0
        t_pointer = 0
        
        while s_pointer < len(s) or t_pointer < len(t):
            if s_pointer < len(s): 
                if s[s_pointer] != '#' :
                    s_stack.append(s[s_pointer])
                else:
                    if s_stack:s_stack.pop()
                s_pointer += 1
                
            if t_pointer < len(t):
                if t[t_pointer] != '#' :
                    t_stack.append(t[t_pointer])
                else:
                    if t_stack:t_stack.pop()
                t_pointer += 1
                
        return "".join(s_stack) == "".join(t_stack)
                
            
        
        
        