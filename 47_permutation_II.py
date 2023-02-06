from typing import List, Dict
from collections import Counter

def permuteUnique(nums: List[int]) -> List[List[int]]:
    res = []
    def dfs(nums_dict: Dict[int, int], intermediate: List[int]):
        if len(intermediate) == len(nums):
            res.append(list(intermediate)) # use list() to create a copy instead of passing a reference
            return

        for num in nums_dict:
            if nums_dict[num] > 0:
                intermediate.append(num)
                nums_dict[num] -= 1
                dfs(nums_dict, intermediate)
                intermediate.pop() # recover the intermediate list and nums dict for other backtracking
                nums_dict[num] += 1
    
    dfs(Counter(nums), [])
    return res
        

nums = [1,1,2]
print(permuteUnique(nums)) # [[1,1,2], [1,2,1], [2,1,1]]

nums = [1,2,3]
print(permuteUnique(nums)) # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]