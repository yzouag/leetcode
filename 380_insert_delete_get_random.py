from random import choice
class RandomizedSet:

    def __init__(self):
        # element and its corresponding position in list
        # the position is for list deletion later
        self.elements = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.elements:
            return False
        self.elements[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.elements:
            return False
        last_num = self.nums[-1]
        # key part: swap node and then pop to make O(1) deletion of list
        self.nums[self.elements[val]], self.nums[-1] = self.nums[-1], self.nums[self.elements[val]]
        self.nums.pop()
        self.elements[last_num] = self.elements[val]
        self.elements.pop(val)
        return True

    def getRandom(self) -> int:
        return choice(self.nums)

randomizedSet = RandomizedSet()
randomizedSet.insert(1) # Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2) # Returns false as 2 does not exist in the set.
randomizedSet.insert(2) # Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom() # getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1) # Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2) # 2 was already in the set, so return false.
randomizedSet.getRandom() # Since 2 is the only number in the set, getRandom() will always return 2.