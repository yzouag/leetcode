from collections import defaultdict


def numRollsToTarget(n: int, k: int, target: int) -> int:
    # starting point: ???
    # a[n+1][target] = sum(a[n][target-1] ... a[n][target-k])
    # a[n][target+1] = a[n][target]

    # first check all invalid poss target
    if target < n or target > n * k:
        return 0
    
    memo = defaultdict(int)
    for i in range(1, k+1):
        memo[(1, i)] = 1
    for i in range(2, n+1):
        for j in range(i, i*k+1):
            memo[(i, j)] = sum([memo[(i-1, l)] for l in range(max(1, j-k) , j)])
    return memo[(n, target)] % (10**9 + 7)
    

n = 1
k = 6
target = 3
print(numRollsToTarget(n, k, target))
# Output: 1

n = 2
k = 6
target = 7
print(numRollsToTarget(n, k, target))
# Output: 6

n = 30
k = 30
target = 500
print(numRollsToTarget(n, k, target))
# Output: 222616187