from typing import List
from collections import defaultdict

def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    # approach 1: BFS
    adjacent_list = defaultdict(list)
    for source, dest, price in flights:
        adjacent_list[source].append((dest, price))

    prices = {}
    stack = [(src, 0)]
    stops = 0
    while stack and stops <= k:
        temp = []
        for node, price in stack:
            for neighbor, weight in adjacent_list[node]:
                if neighbor in prices and prices[neighbor] < price + weight:
                    continue
                temp.append((neighbor, price+weight))
                prices[neighbor] = price+weight
        stops += 1
        stack = temp
    return prices[dst] if dst in prices else -1

    # approach 2: Bellman Ford


n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
print(findCheapestPrice(n, flights, src, dst, k)) # 700

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1
print(findCheapestPrice(n, flights, src, dst, k)) # 200

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 0
print(findCheapestPrice(n, flights, src, dst, k)) # 500