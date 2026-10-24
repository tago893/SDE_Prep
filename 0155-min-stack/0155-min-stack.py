class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, value: int) -> None:
        min_value = self.getMin()
        if min_value == None or min_value>value:
            min_value = value
        self.stack.append((value,min_value))

    def pop(self) -> None:
        self.stack.pop()        

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1][1]


# 1 --> []
# 2 --> [-2], minele = -2
# 3--> [-2,0]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()