class MinStack:

    # def __init__(self):
    #     self.arr = []

    # def push(self, val: int) -> None:
    #     self.arr.append(val)
    #     curr = len(self.arr) - 1
    #     parent = (curr - 1) // 2
    #     while parent >= 0 and self.arr[curr] < self.arr[parent]:
    #         self.arr[curr], self.arr[parent] = self.arr[parent], self.arr[curr]
    #         curr = parent
    #         parent = (curr-1) // 2

    # def pop(self) -> None:
    #     self.arr[0] = self.arr[-1]
    #     self.arr.pop()
    #     end = len(self.arr)
    #     curr = 0
    #     while True:
    #         child_1 = curr*2+1
    #         child_2 = child_1+1
    #         if child_1 >= end:
    #             break
    #         if child_2 >= end:
    #             if self.arr[child_1] < self.arr[curr]:
    #                 self.arr[curr], self.arr[child_1] = self.arr[child_1], self.arr[curr]
    #             break
    #         if self.arr[child_1] < self.arr[child_2]:
    #             self.arr[curr], self.arr[child_1] = self.arr[child_1], self.arr[curr]
    #             curr = child_1
    #         else:
    #             self.arr[curr], self.arr[child_2] = self.arr[child_2], self.arr[curr]
    #             curr = child_2

    # def top(self) -> int:
    #     return self.arr[-1]

    # def getMin(self) -> int:
    #     return self.arr[0]
    def __init__(self):
        self.arr = []
        self.min_val = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if not self.min_val:
            self.min_val.append(val)
        else:
            if val < self.min_val[-1]:
                self.min_val.append(val)
            else:
                self.min_val.append(self.min_val[-1])

    def pop(self) -> None:
        self.arr.pop()
        self.min_val.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.min_val[-1]

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-1)
minStack.getMin()   # return -3
minStack.top()      # return 0
minStack.pop()
minStack.getMin()   # return -2
