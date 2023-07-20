# 1. using the orderedDict (cheating solution)
# 2. using the Dict + double linked list
# Why double linked list? 
#   it can insert or delete itself without using other nodes 
#   (think about how to get the previous node in single link list) 

from typing import Dict


class Node:
    def __init__(self, key, value, prev=None, post=None) -> None:
        self.key: int = key
        self.val: int = value
        self.prev: Node = prev
        self.post: Node = post

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.keyNodeMap: Dict[int, Node] = {}
        
        # using the dummy nodes to avoid edge cases
        self.head: Node = Node(0,0)
        self.tail: Node = Node(0,0)
        self.head.post = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.keyNodeMap:
            return -1
        node = self.keyNodeMap[key]
        # put node to the front of linked list by remove it and then add it to front
        self.__remove(node)
        self.__add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.keyNodeMap:
            # create new node and add to front of queue
            newNode = Node(key, value)
            self.__add(newNode)
            self.keyNodeMap[key] = newNode
            # if exceeds max capacity, pop the last of the node
            if len(self.keyNodeMap) > self.capacity:
                lastNode = self.tail.prev
                self.__remove(lastNode)
                self.keyNodeMap.pop(lastNode.key)
        else:
            # same as get
            node = self.keyNodeMap[key]
            self.__remove(node)
            self.__add(node)
            node.val = value
    
    def __add(self, node: Node) -> None:
        node.post = self.head.post
        node.prev = self.head
        self.head.post = node
        node.post.prev = node

    def __remove(self, node: Node) -> None:
        node.prev.post = node.post
        node.post.prev = node.prev

lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
lRUCache.get(1)
lRUCache.put(3, 3)
lRUCache.get(2)
lRUCache.put(4, 4)
lRUCache.get(1)
lRUCache.get(3)
lRUCache.get(4)