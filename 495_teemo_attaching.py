from typing import List

def findPoisonedDuration(timeSeries: List[int], duration: int) -> int:
    total_poison_time = 0
    poison_end = -1
    for time in timeSeries:
        if time > poison_end:
            total_poison_time += duration
        else:
            total_poison_time += time + duration  - poison_end - 1
        poison_end = time + duration - 1

    return total_poison_time


timeSeries = [1,4]
duration = 2
print(findPoisonedDuration(timeSeries, duration))
# Output: 4

timeSeries = [1,2]
duration = 2
print(findPoisonedDuration(timeSeries, duration))
# Output: 3