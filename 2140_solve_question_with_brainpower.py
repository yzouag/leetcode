from typing import List

def mostPoints(questions: List[List[int]]) -> int:
    memo = {}
    n = len(questions)
    def dfs(i):
        if i >= n:
            return 0
        if i in memo:
            return memo[i]
        memo[i] = max(questions[i][0]+dfs(i+questions[i][1]+1), dfs(i+1))
        return memo[i]
    return dfs(0)

questions = [[3,2],[4,3],[4,4],[2,5]]
print(mostPoints(questions))
# Output: 5

questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
print(mostPoints(questions))
# Output: 7