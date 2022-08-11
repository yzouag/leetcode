from typing import List

from flask import current_app

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # method 1:
        # farthest_index_to_reach = 0
        # for current_index, n in enumerate(nums):
        #     if current_index > farthest_index_to_reach:
        #         return False
        #     farthest_index_to_reach = max(farthest_index_to_reach, current_index+n)
        # return True

        # method 2:
        goal = len(nums) - 1 # initial goal, reach the end
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i # goal is now to reach index i
        return goal == 0

if __name__ == "__main__":
    nums = [2,3,1,1,4]
    assert True == Solution().canJump(nums)

    nums = [3,2,1,0,4]
    assert False == Solution().canJump(nums)