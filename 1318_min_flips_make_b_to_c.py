def minFlips(a: int, b: int, c: int) -> int:
    t = a & b
    k = (a | b) ^ c
    res = 0
    while k != 0:
        if k % 2 == 1:
            if t % 2 == 1:
                res += 2
            else:
                res += 1
        k >>= 1
        t >>= 1
    return res

a = 2
b = 6
c = 5
print(minFlips(a, b, c))
# Output: 3

a = 4
b = 2
c = 7
print(minFlips(a, b, c))
# Output: 1

a = 1
b = 2
c = 3
print(minFlips(a, b, c))
# Output: 0