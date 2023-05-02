def numberOfArrays(s: str, k: int) -> int:
    n = len(s)
    dp = [0] * (n+1)
    dp[0] = 1
    k_length = len(str(k))
    for i in range(1, n+1):
        j = i
        while j >= 1:
            if i-j+1 > k_length:
                break
            if s[j-1] != '0' and int(s[j-1:i]) <= k and int(s[j-1:i]) >= 1:
                dp[i] += dp[j-1]
            j -= 1
    return dp[-1] % (10**9+7)

s = "1000"
k = 10000
print(numberOfArrays(s, k))
# Output: 1

s = "1000"
k = 10
print(numberOfArrays(s, k))
# Output: 0

s = "1317"
k = 2000
print(numberOfArrays(s, k))
# Output: 8

s = "2020"
k = 30
print(numberOfArrays(s, k))
# Output: 1
