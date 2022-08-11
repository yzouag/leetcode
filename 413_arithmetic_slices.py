from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        return 0

if __name__ == "__main__":
    nums = [1,2,3,4]
    assert Solution().numberOfArithmeticSlices(nums) == 3

    nums = [1]
    assert Solution().numberOfArithmeticSlices(nums) == 0