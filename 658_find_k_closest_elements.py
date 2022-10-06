from typing import List
def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    left, right = 0, len(arr) - k
    while left < right:
        mid = (left + right) // 2
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid
    return arr[left:left + k]

arr = [1,2,3,4,5]
k = 4
x = 3
print(findClosestElements(arr, k, x))
# Output: [1,2,3,4]

arr = [1,2,3,4,5]
k = 4
x = -1
print(findClosestElements(arr, k, x))
# Output: [1,2,3,4]