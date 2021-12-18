def evalRPN(tokens):
    stack = []
    result = 0
    while tokens:
        #print(stack,tokens)
        if tokens[0] == "+" or tokens[0] == "-" or tokens[0] == "*" or tokens[0] == "/" :
            if tokens[0] == "+":
                x = stack[-1]
                y = stack[-2]
                # result += (int(x)+int(y))
                stack.pop()
                stack.pop()
                stack.append(int(x)+int(y))
                tokens.remove(tokens[0])
            elif tokens[0] == "-":
                x = stack[-1]
                y = stack[-2]
                # result += (int(x)-int(y))
                stack.pop()
                stack.pop()
                stack.append(int(y)-int(x))
                tokens.remove(tokens[0])
            elif tokens[0] == "*":
                x = stack[-1]
                y = stack[-2]
                # result += (int(x)-int(y))
                stack.pop()
                stack.pop()
                stack.append(int(int(y)*int(x)))
                tokens.remove(tokens[0])
            elif tokens[0] == "/":
                x = stack[-1]
                y = stack[-2]
                # result += (int(x)-int(y))
                stack.pop()
                stack.pop()
                stack.append(int(int(y)/int(x)))
                tokens.remove(tokens[0])
        else:
            stack.append(tokens[0])
            tokens.remove(tokens[0])
            
    return stack[0]
            
example = evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print(example)