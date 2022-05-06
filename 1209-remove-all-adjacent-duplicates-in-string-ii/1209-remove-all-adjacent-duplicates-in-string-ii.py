class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []
        s = list(s)
        s.reverse()
        
        while s:
            # print(stack,s[-1])
            if not stack:
                ch = s.pop()
                stack.append((ch,1))
            else:
                char = s.pop()
                if stack[-1][0] == char:
                    ch,count = stack[-1]
                    stack[-1] = (ch,count+1)
                else:
                    stack.append((char,1))
            
            if stack[-1][1] == k:
                stack.pop()



                
        final = []
        
        for char,count in stack:
            for i in range(count):
                final.append(char)
        
        return "".join(final)
        
        