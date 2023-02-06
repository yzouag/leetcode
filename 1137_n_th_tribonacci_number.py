def tribonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    t0 = 0
    t1 = t2 = 1
    for _ in range(n-2):
        # temp = t2
        # t2 = t0 + t1 + t2
        # t0 = t1
        # t1 = temp
        t0, t1, t2 = t1, t2, t0+t1+t2
    return t2

n = 4
print(tribonacci(n)) # 4

n = 25
print(tribonacci(n)) # 1389537