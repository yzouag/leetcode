from typing import List
def minCost(colors: str, neededTime: List[int]) -> int:
    min_cost_time = 0
    i = 0
    while i < len(colors)-1:
        current_max = neededTime[i]
        while i < len(colors)-1 and colors[i] == colors[i+1]:
            if current_max <= neededTime[i+1]:
                min_cost_time += current_max
                current_max = neededTime[i+1]
            else:
                min_cost_time += neededTime[i+1]
            i += 1
        i += 1
    return min_cost_time

colors = "abaac"
neededTime = [1,2,3,4,5]
print(minCost(colors, neededTime))
# Output: 3

colors = "abc"
neededTime = [1,2,3]
print(minCost(colors, neededTime))
# Output: 0

colors = "aabaa"
neededTime = [1,2,3,4,1]
print(minCost(colors, neededTime))
# Output: 2