from collections import defaultdict
from typing import List
import heapq

def gift_card():
    N, M = input().split(" ")
    N = int(N)
    M = int(M)
    
    if M % 10 != 0:
        return 0
    
    # x + y + z = N
    # 10x + 30y + 50z = M
    # 5N-M/10 = 4x + 2y

    target = 5 * N - M//10
    counts = 0
    for x in range(target//4+1):
        if (target - 4*x)%2 == 0 and x+(target-4*x)//2 <= N:
            print(f'{x} {(target-4*x)//2}')
            counts += 1
    print(counts)


gift_card()

def dijkstra_algo(startNode: str, endNode: str, paths: List[tuple]):
    # build the graph
    adjacentMatrix = defaultdict(list)
    for start, end, distance in paths:
        adjacentMatrix[start].append((end, distance))
    
    # init distances of all points to infinity, startpoint as 0
    distances = {vertex: float('inf') for vertex in adjacentMatrix}
    distances[startNode] = 0
    
    # priority queue for smallest distance
    candidates = [(0, startNode)]
    
    # pick the smallest distance node, update the smallest distance priority queue
    while candidates:
        currentNode, currentDistance = heapq.heappop(candidates)
        if currentNode == endNode:
            return currentDistance
        # we may visit node several times, and they all added to the priority queue
        # so we only use the node with smallest distance (others just discarded)
        # if statement becomes true when we have already included the point to shortest graph
        if currentDistance > distances[currentNode]:
            continue

        for neighbor, dist in adjacentMatrix[currentNode]:
            newDist = currentDistance + dist
            if newDist < distances[neighbor]:
                distances[neighbor] = newDist
                heapq.heappush(candidates, (newDist, neighbor))
    return -1

def clean_dust():
    l = input().split(" ")
    n_workers, n_streets = int(l[0]), int(l[1])
    streets = [0] * (n_streets + 1)
    for _ in range(n_workers):
        l = input().split(" ")
        streets[int(l[0])] += 1
        streets[int(l[1])+1] -= 1
    s = 0
    res = 0
    for i in range(n_streets):
        s += streets[i]
        if s == 0:
            res += 1
    print(res)
# clean_dust()