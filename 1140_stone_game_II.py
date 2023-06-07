from typing import List
def stoneGameII(piles: List[int]) -> int:
    n = len(piles)
    # dp[p][i][m], p denotes either Alice or Bob's term, i is the current pile, m is the number of piles possible to take
    # dp[p][i][m] is the best possible profit for Alice to get given p, i, m
    dp = [[[-1] * (n + 1) for i in range(n + 1)] for p in range(0, 2)]

    def f(p, i, m):
        if i == n:
            return 0
        if dp[p][i][m] != -1:
            return dp[p][i][m]
        res = 1000000 if p == 1 else -1
        s = 0
        for x in range(1, min(2 * m, n - i) + 1):
            s += piles[i + x - 1]
            if p == 0:
                res = max(res, s + f(1, i + x, max(m, x)))
            else:
                res = min(res, f(0, i + x, max(m, x)))
        dp[p][i][m] = res
        return res
    
    return f(0, 0, 1)

piles = [2,7,9,4,4]
print(stoneGameII(piles))
# Output: 10

piles = [1,2,3,4,5,100]
print(stoneGameII(piles))
# Output: 104