class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0]*k
        self.front = -1
        self.back = -1
        self.size = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            if self.isEmpty():
                self.front = 0
                self.back = 0
            elif self.back < self.size -1:
                self.back += 1
            else:
                self.back = 0
            self.queue[self.back] = value
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            if self.front == self.back:
                self.front = -1
                self.back = -1
            elif self.front < self.size -1:
                self.front += 1
            else:
                self.front = 0
            return True

    def Front(self) -> int:
        if not self.isEmpty():
            return self.queue[self.front]
        else:
            return -1
        

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.queue[self.back]
        else:
            return -1

    def isEmpty(self) -> bool:
        if self.front == -1:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.front == self.back + 1 or (self.front == 0 and self.back == self.size-1):
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