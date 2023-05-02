def addDigits(num: int) -> int:
    while num > 9:
        digits = 0
        while num > 9:
            digits += num%10
            num //= 10
        num += digits
    return num

num = 38
print(addDigits(num))
# Output: 2

num = 0
print(addDigits(num))
# Output: 0