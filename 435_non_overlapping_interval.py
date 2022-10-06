from typing import List

def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    # greedy, sort by the ending time
    # assume we choose another interval y with y[end] > current interval x[end]
    # two possibilities: 
    #   1. y[start] >= x[end], then we can still include x into the intervals, no influence to the rest, this case we ignore
    #      which means we lose 1 interval
    #   2. y[start] < x[end] then, if we choose x we cannot choose y, but choosing y means the rest
    #      of intervals can only start from [y:] which is less than [x:], so x must be better
    intervals.sort(key=lambda x: x[1])
    end = intervals[0][1]
    res = 0
    for i in range(1, len(intervals)):
        if intervals[i][0] < end:
            res += 1
        else:
            end = intervals[i][1]
    return res

intervals = [[1,2],[2,3],[3,4],[1,3]]
print(eraseOverlapIntervals(intervals))
# Output: 1

intervals = [[1,2],[1,2],[1,2]]
print(eraseOverlapIntervals(intervals))
# Output: 2

intervals = [[1,2],[2,3]]
print(eraseOverlapIntervals(intervals))
# Output: 0

intervals = [[0,2],[1,3],[2,4],[3,5],[4,6]]
print(eraseOverlapIntervals(intervals))
# Output: 2