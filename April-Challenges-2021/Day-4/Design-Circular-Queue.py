class MyCircularQueue:

    def __init__(self, k: int):
        self.items = k * [None]
        self.maxSize = k
        self.start = -1
        self.top = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            if self.top+1==self.maxSize:
                self.top = 0
            else:
                self.top+=1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value 
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start+1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None            
            # return firstElement
            return True
                

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.items[self.start] 

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.items[self.top]

    def isEmpty(self) -> bool:
        return self.top == -1  

    def isFull(self) -> bool:
        if self.top+1==self.start:
            return True
        elif self.start==0 and self.top+1==self.maxSize:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
