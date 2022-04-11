class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ']':
                if i.isdigit():
                    if not stack:
                        stack.append(i)
                    else:
                        if stack[-1].isdigit(): 
                            stack[-1] = stack[-1] + i
                        else:
                            stack.append(i)
                else:
                    stack.append(i)
            else:
                string = ""
                while stack[-1] != '[':
                    string = stack.pop() + string
                stack.pop()
                no = stack.pop()
                string = int(no) * string
                stack.append(string)
                
        return ''.join(stack)
                
        
        