from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[x] = nums[i+1]
                x += 1
        return x

if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert Solution().removeDuplicates(nums) == 5

    nums = [1, 1, 2]
    assert Solution().removeDuplicates(nums) == 2
