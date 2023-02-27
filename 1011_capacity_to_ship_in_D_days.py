import math
from typing import List
def shipWithinDays(weights: List[int], days: int) -> int:
    def need_days(cap):
        days = 1
        running_sum = 0
        for w in weights:
            running_sum += w
            if running_sum > cap:
                running_sum = w
                days += 1
        return days
        
    left = max(weights)
    right = sum(weights)
    while left < right:
        mid = (left + right) // 2
        if need_days(mid) > days:
            left = mid + 1
        else:
            right = mid
    return left

weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
print(shipWithinDays(weights, days))
# Output: 15

weights = [3,2,2,4,1,4]
days = 3
print(shipWithinDays(weights, days))
# Output: 6

weights = [1,2,3,1,1]
days = 4
print(shipWithinDays(weights, days))
# Output: 3