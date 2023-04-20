import math
def numSquares(n: int) -> int:
    # memo = {}

    # def dfs(n):
    #     if n in memo:
    #         return memo[n]
        
    #     largest_root = math.floor(math.sqrt(n))
    #     if largest_root**2 == n:
    #         memo[n] = 1
    #         return 1
        
    #     res = float('inf')
    #     for i in range(1, largest_root+1):
    #         res = min(res, dfs(n - i**2))
        
    #     memo[n] = res+1
    #     return memo[n]

    # return dfs(n)

    dp = [0] + [float('inf')] * n
    for i in range(1, n+1):
        j = 1
        while j*j <= i:
            dp[i] = min(dp[i], dp[i-j*j]+1)
            j += 1
    return dp[-1]

n = 12
print(numSquares(n))
# Output: 3

n = 13
print(numSquares(n))
# Output: 2