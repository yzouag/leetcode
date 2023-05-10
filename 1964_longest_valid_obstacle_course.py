from typing import List
import bisect

def longestObstacleCourseAtEachPosition(obstacles: List[int]) -> List[int]:
    # n = len(obstacles)
    # dp = [1] * n
    # for i in range(1, n):
    #     longest = 1
    #     for j in range(i):
    #         if obstacles[i] >= obstacles[j]:
    #             longest = max(longest, dp[j]+1)
    #     dp[i] = longest
    # return dp
    
    lis = [] # lis[i] means, for a sequence of length i+1, its last height is lis[i]
    res = []
    for obstacle in obstacles:
        index = bisect.bisect_right(lis, obstacle) # current obstacle could be inserted in index
        if index >= len(lis): # if this index is the end of lis, append this obstacle
            lis.append(obstacle)
        else: # lis[index] used to be in some height larger than obstacle
              # so for later obstacles, they are better to follow this lower obstacle, not the large one
              # [3,1,5,6] when we want to insert 1, that lis [3] which means the length 1 obstacle ends with 3
              # since now we have a obstacle of height 1, later obstacles can pick 1 instead of 3
              # so lis changes to [1]
            lis[index] = obstacle
        res.append(index+1)
    return res

obstacles = [1,2,3,2]
print(longestObstacleCourseAtEachPosition(obstacles))
# Output: [1,2,3,3]

obstacles = [2,2,1]
print(longestObstacleCourseAtEachPosition(obstacles))
# Output: [1,2,1]

obstacles = [3,1,5,6,4,2]
print(longestObstacleCourseAtEachPosition(obstacles))
# Output: [1,1,2,3,2,2]