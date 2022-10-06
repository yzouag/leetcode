from typing import Optional
class LinkNode:
    def __init__(self, key: int, value: int, next=None) -> None:
        self.key = key
        self.next = next
        self.value = value

# few things about make a hashmap
# 1. most important, we need a hash function. here we use multiplicative hash function
#    the divider (or the size of array) must be a prime number (avoid collision)
# 2. if collision does happen, we need to maintain a link list to store all these collided nodes
#    here the linked list is made by ourselves, we can also use deque
# 3. every time when a new item is put, it should be at the front of the list, so we can access 
#    it most quickly

class MyHashMap:
    
    def hash(self, key: int) -> int:
        return key * self.multiplication % self.size
            
    def __init__(self):
        self.size = 19997
        self.multiplication = 12582917
        self.data = [None] * self.size

    def put(self, key: int, value: int) -> None:
        self.remove(key) # remove the key first, and add the new node to the front
        pos = self.hash(key)
        node = LinkNode(key, value, self.data[pos])
        self.data[pos] = node

    def get(self, key: int) -> int:
        head = self.data[self.hash(key)]
        while head:
            if head.key == key:
                return head.value
            head = head.next
        return -1

    def remove(self, key: int) -> None:
        pos = self.hash(key)
        head = self.data[pos]
        if head is None:
            return
        if head.key == key:
            self.data[pos] = head.next
            return

        while head.next:
            if head.next.key == key:
                head.next = head.next.next
            else:
                head = head.next
        


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.remove(65513)
obj.put(3, 5)
param_2 = obj.get(3)
print(param_2)
obj.remove(3)