from typing import List

# The trick is to keep a counter of the numbers. 
# If we see one number the counter should be 1, if we see two numbers the counter should be 2, 
# and if we see 3 numbers the counter should loop back to 0. 
# 
# In order to have these 3 states we need 2 bits, hence a and b. 
# Below is the transition table, and the code follows from it. 
# It should be obvious if we figure it out for a single bit we can apply to 32-bits. 
# Note that the order of operations matter, we calculate b first and then a. 
# Since we're guaranteed three numbers and a single lone number, we can just return b (ab will never end up as 10).

# a b num -> a b
# 0 0 0   -> 0 0 
# 0 1 0   -> 0 1
# 1 0 0   -> 1 0
# 0 0 1   -> 0 1
# 0 1 1   -> 1 0
# 1 0 1   -> 0 0
def singleNumber(nums: List[int]) -> int:
    a = b = 0
    for n in nums:
        b = (b^n)&~a
        a = (a^n)&~b
    return b

nums = [2,2,3,2]
print(singleNumber(nums))
# Output: 3

nums = [0,1,0,1,0,1,99]
print(singleNumber(nums))
# Output: 99