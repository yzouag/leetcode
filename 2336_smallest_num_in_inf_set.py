class SmallestInfiniteSet:

    def __init__(self):
        self.popped = set()
        self.i = 1

    def popSmallest(self) -> int:
        res = self.i
        self.popped.add(self.i)
        while self.i in self.popped:
            self.i += 1
        return res

    def addBack(self, num: int) -> None:
        self.popped.discard(num)
        if self.i >= num:
            self.i = num
        


smallestInfiniteSet = SmallestInfiniteSet()
smallestInfiniteSet.addBack(2)      # 2 is already in the set, so no change is made.
smallestInfiniteSet.popSmallest()   # return 1, since 1 is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest()   # return 2, and remove it from the set.
smallestInfiniteSet.popSmallest()   # return 3, and remove it from the set.
smallestInfiniteSet.addBack(1)      # 1 is added back to the set.
smallestInfiniteSet.popSmallest()   # return 1, since 1 was added back to the set and
                                    # is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest()   # return 4, and remove it from the set.
smallestInfiniteSet.popSmallest()   # return 5, and remove it from the set.