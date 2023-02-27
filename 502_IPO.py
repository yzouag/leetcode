from typing import List
import heapq
def findMaximizedCapital(k: int, w: int, profits: List[int], capital: List[int]) -> int:
    profit_capital = list(zip(capital, profits))
    profit_capital.sort()
    available_projects = 0
    available_profits = []
    for _ in range(k):
        while available_projects < len(profit_capital):
            cap, prof = profit_capital[available_projects]
            if cap <= w:
                heapq.heappush(available_profits, -prof)
                available_projects += 1
            else:
                break
        if len(available_profits) == 0:
            return w
        w += -heapq.heappop(available_profits)
    return w

k = 2
w = 0
profits = [1,2,3]
capital = [0,1,1]
print(findMaximizedCapital(k, w, profits, capital))
# Output: 4

k = 3
w = 0
profits = [1,2,3]
capital = [0,1,2]
print(findMaximizedCapital(k, w, profits, capital))
# Output: 6