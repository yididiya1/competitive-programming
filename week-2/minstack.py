class MinStack:

    def __init__(self):
        self.stack = []   

    def push(self, val: int) -> None:
        return self.stack.append(val)

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)



obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(3)
parma_2 = obj.getMin()
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()

print(parma_2,param_3,param_4)