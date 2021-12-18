class MyQueue:

    def __init__(self):
        self.stack = []
        self.reversed = []
        self.lastElemenet = None

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.lastElement = x
        self.stack.append(x)

    def pop(self) -> int:
        if len(self.reversed) == 0:
            while len(self.stack) > 0:
                self.reversed.append(self.stack.pop())
        return self.reversed.pop()

    def peek(self) -> int:
        if len(self.reversed) != 0:
            return self.reversed[-1]
        return self.lastElement

    def empty(self) -> bool:
        return not self.stack and not self.reversed 
        



obj = MyQueue()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()

print(param_2,param_3,param_4)