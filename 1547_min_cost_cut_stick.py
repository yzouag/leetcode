from typing import List, Tuple
import bisect

def minCost(n: int, cuts: List[int]) -> int:
    cuts = [0] + sorted(cuts) + [n]
    memo = {}

    def dfs(left, right):
        # base case, no more cuts needed
        if right - left == 1:
            return 0
        
        if (left, right) in memo:
            return memo[(left, right)]

        # recursion: any cut between left and right
        min_cost = min([dfs(left, i) + dfs(i, right) + cuts[right] - cuts[left] for i in range(left+1, right)])
        memo[(left, right)] = min_cost
        return memo[(left, right)]
    return dfs(0, len(cuts)-1)

n = 7
cuts = [1,3,4,5]
print(minCost(n, cuts))
# Output: 16

n = 9
cuts = [5,6,1,4,2]
print(minCost(n, cuts))
# Output: 22