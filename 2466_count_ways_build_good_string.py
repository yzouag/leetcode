def countGoodStrings(low: int, high: int, zero: int, one: int) -> int:
    dp = [0] * (1+high)
    dp[0] = 1
    for i in range(1, 1+high):
        if i >= zero:
            dp[i] += dp[i-zero]
        if i >= one:
            dp[i] += dp[i-one]
    return sum(dp[low:high+1]) % (10**9+7)

low = 3
high = 3
zero = 1
one = 1
print(countGoodStrings(low, high, zero, one))
# Output: 8

low = 2
high = 3
zero = 1
one = 2
print(countGoodStrings(low, high, zero, one))
# Output: 5