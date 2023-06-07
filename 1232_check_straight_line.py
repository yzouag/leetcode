from typing import List
def checkStraightLine(coordinates: List[List[int]]) -> bool:
    diff = (coordinates[1][0]-coordinates[0][0], coordinates[1][1]-coordinates[0][1])
    for coord in coordinates[2:]:
        if (coord[0] - coordinates[0][0]) * diff[1] != (coord[1] - coordinates[0][1]) * diff[0]:
            return False
    return True

coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
print(checkStraightLine(coordinates))
# Output: true

coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
print(checkStraightLine(coordinates))
# Output: false