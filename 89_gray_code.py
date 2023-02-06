from typing import List
def grayCode(n: int) -> List[int]:
    if n == 0: return [0]
    t = grayCode(n-1)
    return t + [i+(1<<(n-1)) for i in t][::-1]

n = 2
print(grayCode(n)) # Output: [0,1,3,2]

n = 1
print(grayCode(n)) # Output: [0,1]