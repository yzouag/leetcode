from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    res = []

    def backtracking(candidates, temp_list, current_target) -> None:
        for i in range(len(candidates)):
            if current_target - candidates[i] == 0:
                res.append(temp_list + [candidates[i]]) # must use list + list, it will return a copy
            elif current_target - candidates[i] > 0:
                backtracking(candidates[i:], temp_list + [candidates[i]], current_target-candidates[i])

    backtracking(candidates, [], target)
    return res


candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates, target))
# Output: [[2,2,3],[7]]

candidates = [2,3,5]
target = 8
print(combinationSum(candidates, target))
# Output: [[2,2,2,2],[2,3,3],[3,5]]

candidates = [2]
target = 1
print(combinationSum(candidates, target))
# Output: []