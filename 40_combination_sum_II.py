from typing import List


def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    res = []
    candidates.sort()
    n = len(candidates)

    def backtracking(temp: List[int], curr_target: int, start: int, res: List[List[int]], candidates: List[int]):
        if curr_target == 0:
            res.append(temp)
            return

        for i in range(start, n):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] > curr_target:
                break
            backtracking(temp + [candidates[i]], curr_target-candidates[i], i+1, res, candidates)

    backtracking([], target, 0, res, candidates)
    return res


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(combinationSum2(candidates, target))
# Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

candidates = [2,5,2,1,2]
target = 5
print(combinationSum2(candidates, target))
# Output: [[1,2,2], [5]]

candidates = [1, 1, 1]
target = 3
print(combinationSum2(candidates, target))
# Output: [[1,1,1]]