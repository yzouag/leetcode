from typing import List
import heapq
def getSkyline(buildings: List[List[int]]) -> List[List[int]]:
    result = []
    heapq.heappush
    result.append(buildings[i][0], buildings[i][2])
    right_end = []
    right_end.append(buildings[i][1], buildings[i][2])
    for i in range(1, len(buildings)):
        if buildings[i][0] == result[-1][0]:
            if buildings[i][2] > result[-1][1]:
                result[-1][1] = buildings[i][2]
        

buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
print(getSkyline(buildings))
# Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]

buildings = [[0,2,3],[2,5,3]]
print(getSkyline(buildings))
# Output: [[0,3],[5,0]]