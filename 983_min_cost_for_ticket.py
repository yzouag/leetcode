from typing import List

def mincostTickets(days: List[int], costs: List[int]) -> int:
    memo = {}
    tickets = [(1, costs[0]), (7, costs[1]), (30, costs[2])]
    n = len(days)

    def dfs(index, current_cost) -> int:
        if index == n: # base case
            return current_cost
        min_cost = float('inf')
        for duration, cost in tickets:
            next_index = index
            expiration_day = days[index] + duration
            while next_index < n and days[next_index] < expiration_day:
                next_index += 1
            next_cost = memo[next_index] if next_index in memo else dfs(next_index, current_cost+cost)
            next_cost = dfs(next_index, current_cost+cost)
            min_cost = min(min_cost, next_cost)
        # memo[index] = min_cost
        return min_cost

    return dfs(0, 0)


days = [1,4,6,7,8,20]
costs = [2,7,15]
print(mincostTickets(days, costs))
# Output: 11

days = [1,2,3,4,5,6,7,8,9,10,30,31]
costs = [2,7,15]
print(mincostTickets(days, costs))
# Output: 17