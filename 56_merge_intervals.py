from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    # method 1: sort then merge
    intervals.sort()
    result = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= result[-1][1]:
            if intervals[i][1] > result[-1][1]:
                result[-1][1] = intervals[i][1]
        else:
            result.append(intervals[i])
    return result

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))
# Output: [[1,6],[8,10],[15,18]]

intervals = [[1,4],[4,5]]
print(merge(intervals))
# Output: [[1,5]]