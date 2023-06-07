# hash function:
#   1. mod
#   2. multiplicative
# consideration for hash functions:
#   1. uniform distribution of hash keys, or there will be more hash collisions.
#      hard to ensure in design, but using statistical tools chi-square test
#   2. if using open addressing method, the hash function should also prevent clustering
#
# load factor
#   define as (number of entries occupied) / (number of buckets)
#   dynamic resizing take place when alpha is above or below certain threshold
#   resizing take O(n) time when we try to allocate new buckets and re-compute all hashings
#
# collision resolution
#   1. chaining, linear time for search on chain. Can use other data structures
#      (if key is ordered, using binary search tree. dynamic perfect hashing, use two level hash table)
#   2. open addressing. linear probing (find the next empty slot after current). quardratic probing, double
#      hashing. The performance of probing depends on the load factor. open addressing will be faster than
#      chaining when load factor is small. The worst case could be O(n) when load factor closes to 1.

class MyHashSet:

    def __init__(self):
        self.arr = [None] * 8
        self.capacity = 8
        self.size = 0
        self.thres = 2 / 3
        
    def hash(self, key):
        return key % self.capacity
        
    def rehash(self, key):
        return (5 * key + 1) % self.capacity
    
    def insertPos(self, key):
        pos = self.hash(key)
        #using -1 to represent the "removed" item
        while self.arr[pos] is not None:
            if self.arr[pos] == key: return -1
            if self.arr[pos] == -1: break
            pos = self.rehash(pos)
        return pos
    
    def safeAdd(self, key):
        pos = self.insertPos(key)
        #already in, 
        if pos == -1: return 
        self.arr[pos] = key
        self.size += 1
    
    def safeAddArr(self, arr):
        for val in arr: 
            if val is not None: self.safeAdd(val)

    def add(self, key: int) -> None:
        def preAdd(self):
            if self.size / self.capacity <= self.thres: return 
            self.capacity <<= 1
            oldArr, self.arr = copy.deepcopy(self.arr), [None] * self.capacity
            self.safeAddArr(oldArr)
        
        preAdd(self)
        self.safeAdd(key)
         
    def remove(self, key: int) -> None:
        pos = self.hash(key)
        while self.arr[pos] is not None:
            if self.arr[pos] == key: 
                self.arr[pos] = -1
                self.size -= 1
                return
            pos = self.rehash(pos)
        return

    def contains(self, key: int) -> bool:
        pos = self.hash(key)
        while self.arr[pos] is not None:
            if self.arr[pos] == key: return True
            pos = self.rehash(pos)
        return False


myHashSet = MyHashSet()
myHashSet.add(1) # set = [1]
myHashSet.add(2) # set = [1, 2]
myHashSet.contains(1) # return True
myHashSet.contains(3) # return False, (not found)
myHashSet.add(2) # set = [1, 2]
myHashSet.contains(2) # return True
myHashSet.remove(2) # set = [1]
myHashSet.contains(2) # return False, (already removed)