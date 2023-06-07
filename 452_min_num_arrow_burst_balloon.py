from typing import List
def findMinArrowShots(points: List[List[int]]) -> int:
    # sort by the end of each balloon
    # if we want to shoot as many balloons as possible
    # we need to always shoot at the end of the balloon
    # any balloon after current one, if its starting position is to the left of the current end
    # then it can be included in the current shot
    points.sort(key=lambda x: x[1])
    res = 1
    
    end = points[0][1]
    for point in points[1:]:
        if point[0] <= end:
            continue
        end = point[1]
        res += 1
    return res

points = [[10,16],[2,8],[1,6],[7,12]]
print(findMinArrowShots(points))
# Output: 2

points = [[1,2],[3,4],[5,6],[7,8]]
print(findMinArrowShots(points))
# Output: 4

points = [[1,2],[2,3],[3,4],[4,5]]
print(findMinArrowShots(points))
# Output: 2

points = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]
print(findMinArrowShots(points))
# Output: 2