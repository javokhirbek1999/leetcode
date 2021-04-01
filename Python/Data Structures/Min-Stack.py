class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minval = []

    def push(self, val: int) -> None:
        if len(self.stack)==0:
            self.stack.append(val)
            self.minval.append(val)
        else:
            if self.minval[-1]<val:
                self.minval.append(self.minval[-1])
            else:
                self.minval.append(val)
            self.stack.append(val)
            

    def pop(self) -> None:
        if len(self.stack)==0:
            return -1
        self.stack.pop()
        self.minval.pop()
        

    def top(self) -> int:
        if len(self.stack)==0:
            return -1
        else:
            return self.stack[-1]
            
        

    def getMin(self) -> int:
        if len(self.minval)==0:
            return -1
        else:
            return self.minval[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
