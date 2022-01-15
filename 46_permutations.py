from copy import deepcopy
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        # method 1: recursion
        def get_sub_permute(remains, perm, result):
            if len(remains) == 0: # no word remains, this is one possible permutation, append it to result
                result.append(deepcopy(perm))

            for i in range(len(remains)):
                newRemains = remains[:i] + remains[i+1:] # new remains excludes the number i, this create a new list, not a reference
                perm.append(remains[i])
                get_sub_permute(newRemains, perm, result)
                perm.pop() # pop number in permutation, so the perm keeps the original state
            return result
        return get_sub_permute(nums, [], [])
        """
        # method 2: DFS
        stack = [(nums, [])]
        result = []
        while stack:
            remains, used = stack.pop() # the only difference between DFS and BFS is here, we pop or popleft
            if len(remains) == 0:
                result.append(used)
            else:
                for i in range(len(remains)):
                    new_used = used + [remains[i]]
                    new_remains = remains[:i] + remains[i+1:]
                    stack.append((new_remains, new_used))
        return result

if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution().permute(nums))