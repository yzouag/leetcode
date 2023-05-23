from typing import List
def removeCoveredIntervals(intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x: (x[0], -x[1]))
    res = 0
    end = -1
    for interval in intervals:
        if interval[1] <= end:
            continue
        else:
            res += 1
            end = interval[1]
    return res

intervals = [[1,4],[3,6],[2,8]]
print(removeCoveredIntervals(intervals))
# Output: 2

intervals = [[1,4],[2,3]]
print(removeCoveredIntervals(intervals))
# Output: 1

intervals = [[1,2],[1,4],[3,4]]
print(removeCoveredIntervals(intervals))
# Output: 1