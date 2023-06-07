from typing import List
def stoneGameIII(stoneValue: List[int]) -> str:
    total_points = sum(stoneValue)
    n = len(stoneValue)
    dp = {}

    def dfs(p, i): # best score of alice
        if i >= n:
            return 0
        if (p, i) in dp:
            return dp[(p,i)]
        if p == 0:
            dp[(p,i)] = max([sum(stoneValue[i:i+k]) + dfs(1, i+k) for k in range(1,4)])
        else:
            dp[(p,i)] = min([dfs(0, i+k) for k in range(1,4)])
        return dp[(p,i)]
    
    alice = dfs(0, 0)
    bob = total_points - alice
    if alice > bob:
        return "Alice"
    elif alice == bob:
        return "Tie"
    else:
        return "Bob"

values = [1,2,3,7]
print(stoneGameIII(values))
# Output: "Bob"

values = [1,2,3,-9]
print(stoneGameIII(values))
# Output: "Alice"

values = [1,2,3,6]
print(stoneGameIII(values))
# Output: "Tie"