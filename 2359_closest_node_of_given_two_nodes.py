from typing import List
from collections import defaultdict
def closestMeetingNode(edges: List[int], node1: int, node2: int) -> int:
    set1 = set()
    set2 = set()
    for _ in range(len(edges)):
        if node1 in set2:
            if node2 in set1:
                return min(node1, node2)
            return node1
        set1.add(node1)
        if node2 in set1:
            return node2
        set2.add(node2)
        node1 = edges[node1]
        node2 = edges[node2]
        if node1 in set1 and node2 in set2: # if cycle
            break
    return -1

edges = [2,2,3,-1]
node1 = 0
node2 = 1
print(closestMeetingNode(edges, node1, node2)) # 2

edges = [1,2,-1]
node1 = 0
node2 = 2
print(closestMeetingNode(edges, node1, node2)) # 2

edges = [4,4,8,-1,9,8,4,4,1,1]
node1 = 5
node2 = 6
print(closestMeetingNode(edges, node1, node2)) # 1
