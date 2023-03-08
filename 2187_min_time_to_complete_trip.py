from typing import List


def minimumTime(time: List[int], totalTrips: int) -> int:
    max_time = time[0] * totalTrips
    min_time = 0
    while min_time < max_time:
        mid = (max_time + min_time) // 2
        
        trips = 0
        for trip_time in time:
            trips += mid // trip_time
        
        if trips >= totalTrips:
            max_time = mid
        else:
            min_time = mid + 1
    return max_time


time = [1, 2, 3]
totalTrips = 5
print(minimumTime(time, totalTrips))
# Output: 3

time = [2]
totalTrips = 1
print(minimumTime(time, totalTrips))
# Output: 2
