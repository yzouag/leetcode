def getSmallestString(n: int, k: int) -> str:
    res = ''
    while n > 0:
        ch = max(k-(n-1)*26, 1)
        n = n - 1
        k = k - ch
        res = res + chr(ch-1+97) # 97 = ord('a')
    return res

n = 3
k = 27
print(getSmallestString(n, k))
# Output: "aay"

n = 5
k = 73
print(getSmallestString(n, k))
# Output: "aaszz"