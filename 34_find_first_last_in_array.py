from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = -1, -1
        
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] == target:
                start = mid
                r = mid - 1
            else:
                l = mid + 1

        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] == target:
                end = mid
                l = mid + 1
            else:
                l = mid + 1
        return [start, end]


if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    assert Solution().searchRange(nums, target) == [3, 4]

    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    assert Solution().searchRange(nums, target) == [-1, -1]
