class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        my_dict ={')':'(','}':'{',']':'['}
        strings = list(s)
        print(strings)
        if len(strings)%2 != 0:
            return False
        else:
            counter = 0
            while len(strings)  > counter:
                print(counter)
                if strings[counter] == '(' or strings[counter] == '{' or strings[counter] == '[':
                    stack.append(strings[counter])
                    counter += 1
                elif strings[counter] == ')' or strings[counter] == '}' or strings[counter] == ']':
                    if len(stack) == 0:
                        return False
                    else:
                        before = stack.pop()
                        if before != my_dict[strings[counter]]:
                            return False
                        counter += 1
            
    
            if len(stack) != 0:
                return False
            else:
                return True