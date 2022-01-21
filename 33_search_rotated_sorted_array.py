from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # divide the array to two parts, both sorted array [5,6,7,1,2,3,4] => [5,6,7], [1,2,3,4]
        # if target < nums[0] and mid < nums[0], both on right array (target=2, mid = 1)
        # if target > nums[0] and mid > nums[0], both on left array (target=6, mid = 7)
        # else, they are not in the same array
        # (target=7, mid=1) on the left side
        # (target=2, mid=6) on the right side
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if (nums[mid] < nums[0]) == (target < nums[0]):
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    return mid
            elif target < nums[0]:
                l = mid + 1
            else:
                r = mid - 1
        return -1
        

if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0
    assert Solution().search(nums, target) == 4

    nums = [4,5,6,7,0,1,2]
    target = 3
    assert Solution().search(nums, target) == -1

    nums = [1]
    target = 1
    assert Solution().search(nums, target) == 0

    nums = [1, 3]
    target = 2
    assert Solution().search(nums, target) == -1