from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        left = 0
        right = len(nums) - 1
        while left <= right:
            left_s = nums[left] ** 2
            right_s = nums[right] ** 2
            if left_s <= right_s:
                result.insert(0, right_s)
                right -= 1
            else:
                result.insert(0, left_s)
                left += 1
        return result

if __name__ == "__main__":
    nums = [-4,-1,0,3,10]
    print(Solution().sortedSquares(nums))
    