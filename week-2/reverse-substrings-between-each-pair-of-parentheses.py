def reverseParentheses(s):
    stack = []
    counter = 0
    while counter < len(s):
        #print(stack)
        if s[counter] != ')':
            stack.append(s[counter])

        else :
            temp = []
            while stack :
                if stack[-1] != '(':
                    temp.append(stack.pop())
                else :
                    stack.pop()
                    stack.extend(temp)
                    break
                
        counter += 1
    
    return ''.join(stack)
            

example = reverseParentheses("(u(love)i)")
print(example)