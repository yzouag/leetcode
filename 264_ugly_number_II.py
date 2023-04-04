def nthUglyNumber(n: int) -> int:
    # ugly number = previous ugly number * 2, 3, 5
    # for each ugly number, we have three options *2, *3, *5
    # 1, 2, 3, 4, 5, 6
    # each of them can *2, *3, *5
    # we need to figure out which number should append next
    # for 1, we first *2, now it's smallest, we append 2, then we know that 1 cannot *2 again, so the
    # next number to *2 is 2
    ugly = [1]
    i2 = i3 = i5 = 0
    while len(ugly) < n:
        u2, u3, u5 = ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5
        u_min = min([u2, u3, u5])
        if u2 == u_min:
            i2 += 1
        if u3 == u_min:
            i3 += 1
        if u5 == u_min:
            i5 += 1
        ugly.append(u_min)
    return ugly[-1]

n = 10
print(nthUglyNumber(n))
# Output: 12

n = 1
print(nthUglyNumber(n))
# Output: 1