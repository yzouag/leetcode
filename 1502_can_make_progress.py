from typing import List
def canMakeArithmeticProgression(arr: List[int]) -> bool:
    # arr.sort()
    # diff = arr[1] - arr[0]
    # for i in range(2, len(arr)):
    #     if arr[i] - arr[i-1] != diff:
    #         return False
    # return True

    # O(n) solution using set
    # the property MAX - MIN = N * diff
    min_value, max_value = min(arr), max(arr)
    n = len(arr)
    
    if max_value - min_value == 0:
        return True
    if (max_value - min_value) % (n - 1):

        return False
    
    diff = (max_value - min_value) // (n - 1)
    number_set = set()
    
    for a in arr:
        if (a - min_value) % diff:
            return False
        number_set.add(a)
    
    return len(number_set) == n

arr = [3,5,1]
print(canMakeArithmeticProgression(arr))
# Output: true

arr = [1,2,4]
print(canMakeArithmeticProgression(arr))
# Output: false