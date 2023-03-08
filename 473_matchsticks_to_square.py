from typing import List

def makesquare(matchsticks: List[int]) -> bool:
    # this is a backtracking approach
    # better approach will be dynamic programming
    if len(matchsticks) <= 3 or sum(matchsticks) % 4 != 0:
        return False
    
    sums = [0] * 4
    side_length = sum(matchsticks) // 4
    matchsticks.sort(reverse=True) # consider the longest match stick first, so the depth of recursion will be smaller

    def dfs(i):
        if i == len(matchsticks):
            return sums[0] == sums[1] == sums[2] == sums[3]
        
        for j in range(4):
            if sums[j] + matchsticks[i] <= side_length:
                sums[j] += matchsticks[i]
                if dfs(i+1):
                    return True
                sums[j] -= matchsticks[i]
        return False
    
    return dfs(0)


matchsticks = [1,1,2,2,2]
print(makesquare(matchsticks))
# Output: true

matchsticks = [3,3,3,3,4]
print(makesquare(matchsticks))
# Output: false