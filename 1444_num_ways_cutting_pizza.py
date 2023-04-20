from typing import List

def ways(pizza: List[str], k: int) -> int:
    m, n = len(pizza), len(pizza[0])

    memo = {}
    def dfs(i, j, k):
        if (i, j, k) in memo:
            return memo[(i, j, k)]
        
        if k == 1:
            for x in range(i, m):
                for y in range(j, n):
                    if pizza[x][y] == 'A':
                        memo[(i, j, k)] = 1
                        return 1
            memo[(i, j, k)] = 0
            return 0
        
        res = 0

        has_apple = False
        for x in range(i+1, m):
            if not has_apple:
                for t in range(j, n):
                    if pizza[x-1][t] == 'A':
                        has_apple = True
                        break
            if has_apple:
                res += dfs(x, j, k-1)
        
        has_apple = False
        for y in range(j+1, n):
            if not has_apple:
                for t in range(i, m):
                    if pizza[t][y-1] == 'A':
                        has_apple = True
                        break
            if has_apple:
                res += dfs(i, y, k-1)

        memo[(i, j, k)] = res
        return res
    
    return dfs(0, 0, k)%(10**9+7)

pizza = ["A..","AAA","..."]
k = 3
print(ways(pizza, k))
# Output: 3

pizza = ["A..","AA.","..."]
k = 3
print(ways(pizza, k))
# Output: 1

pizza = ["A..","A..","..."]
k = 1
print(ways(pizza, k))
# Output: 1