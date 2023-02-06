from typing import List
def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    res = []
    for i, interval in enumerate(intervals):
        if interval[1] < newInterval[0]:
            res.append(interval)
        elif interval[0] > newInterval[1]:
            res.append(newInterval)
            res.extend(intervals[i:])
            break
        elif interval[1] > newInterval[0] or interval[0] < newInterval[1]:
            newInterval[0] = min(interval[0], newInterval[0])
            newInterval[1] = max(newInterval[1], interval[1])
    return res

intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(insert(intervals, newInterval)) # Output: [[1,5],[6,9]]

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(insert(intervals, newInterval)) # Output: [[1,2],[3,10],[12,16]]