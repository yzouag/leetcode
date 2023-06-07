from typing import List
def trap(height: List[int]) -> int:
    left, right = 0, len(height)-1
    left_max = right_max = 0
    res = 0
    while left <= right:
        if left_max > right_max:
            if height[right] > right_max:
                right_max = height[right]
            else:
                res += right_max - height[right]
            right -= 1
        else:
            if height[left] > left_max:
                left_max = height[left]
            else:
                res += left_max - height[left]
            left += 1
    return res

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))
# Output: 6

height = [4,2,0,3,2,5]
print(trap(height))
# Output: 9