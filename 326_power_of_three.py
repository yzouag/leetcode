def isPowerOfThree(n: int) -> bool:
    if n == 1:
        return True
    if n <= 0 or n % 3 != 0:
        return False 
    return isPowerOfThree(n//3)

n = 27
print(isPowerOfThree(n))
# Output: true

n = 0
print(isPowerOfThree(n))
# Output: false

n = -1
print(isPowerOfThree(n))
# Output: false