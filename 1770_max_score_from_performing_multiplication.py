from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # # brute force method:
        # def maxScore(nums: List[int], remain_operations: int) -> int:
        #     if remain_operations == 0:
        #         return 0
        #     return max(multipliers[-remain_operations]*nums[0] + maxScore(nums[1:], remain_operations-1), 
        #         multipliers[-remain_operations]*nums[-1] + maxScore(nums[:-1], remain_operations-1))
        # return maxScore(nums, len(multipliers))

        # dynamic programming
        


if __name__ == "__main__":
    nums = [1, 2, 3]
    multipliers = [3, 2, 1]
    assert Solution().maximumScore(nums, multipliers) == 14

    nums = [-5, -3, -3, -2, 7, 1]
    multipliers = [-10, -5, 3, 4, 6]
    assert Solution().maximumScore(nums, multipliers) == 102
