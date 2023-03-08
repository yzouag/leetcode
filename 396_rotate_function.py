from typing import List
def maxRotateFunction(nums: List[int]) -> int:
    # F(0) = 0*a + 1*b + 2*c + 3*d + 4*e
    # F(1) = 0*e + 1*a + 2*b + 3*c + 4*d
    # F(2) = 0*d + 1*e + 2*a + 3*b + 4*c
    # F(1)-F(0) = d + c + b + a - 4e = a + b + c + d + e - 5e
    # F(2)-F(1) = e + a + b + c - 4d = a + b + c + d + e - 5d
    f = 0
    for i, num in enumerate(nums):
        f += i * num
    
    N = len(nums)
    sum_nums = sum(nums)
    res = f
    
    for i in range(1, N):
        f += sum_nums - N * nums[-i]
        res = max(res, f)
    return res

nums = [4,3,2,6]
print(maxRotateFunction(nums))
# Output: 26

nums = [100]
print(maxRotateFunction(nums))
# Output: 0