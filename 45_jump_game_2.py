from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        # method 1:
        # steps = [0] * len(nums)
        # for i in range(len(nums)):
        #     for j in range(1, nums[i]+1):
        #         if i + j < len(nums):
        #             if steps[i+j] == 0 or 1 + steps[i] < steps[i+j]:
        #                 steps[i+j] = 1 + steps[i]
        # return steps[-1]

        # method 2: BFS
        n = len(nums)
        i = 0
        maxReachable = 0
        lastNodeInLevel = 0
        level = 0
        while lastNodeInLevel < n - 1: # for every layer, we are trying to find the largest node to reach in the next level
            maxReachable = max(maxReachable, i + nums[i])
            if i == lastNodeInLevel:
                lastNodeInLevel = maxReachable
                level += 1
            i += 1
        return level
            


if __name__ == "__main__":
    nums = [2,3,1,1,4]
    assert 2 == Solution().jump(nums)

    nums = [2,3,0,1,4]
    assert 2 == Solution().jump(nums)

    nums = [1]
    assert 0 == Solution().jump(nums)