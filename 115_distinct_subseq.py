def numDistinct(s: str, t: str) -> int:
    m = len(s)
    n = len(t)

    memo = {}
    def dfs(i, j):
        if j == n:
            return 1
        if i == m:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]
        res = 0
        if s[i] == t[j]:
            res += dfs(i+1, j+1)
        res += dfs(i+1, j)
        memo[(i, j)] = res
        return res

    return dfs(0, 0)

s = "rabbbit"
t = "rabbit"
print(numDistinct(s, t))
# Output: 3

s = "babgbag"
t = "bag"
print(numDistinct(s, t))
# Output: 5

s = "gbag"
t = "g"
print(numDistinct(s, t))
# Output: 2