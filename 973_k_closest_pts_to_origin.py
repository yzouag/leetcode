from typing import List
import heapq

# note that another solution
#
# quick sort, which the average time complexity is O(n)
# the worst case is O(n^2)
# The advantage of this solution is it is very efficient.
# The disadvatage of this solution are it is neither an online solution 
#   nor a stable one. And the K elements closest are not sorted in ascending order.
def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    return heapq.nsmallest(k, points, key=lambda x: x[0]**2+x[1]**2)

points = [[1,3],[-2,2]]
k = 1
print(kClosest(points, k))
# Output: [[-2,2]]

points = [[3,3],[5,-1],[-2,4]]
k = 2
print(kClosest(points, k))
# Output: [[3,3],[-2,4]]