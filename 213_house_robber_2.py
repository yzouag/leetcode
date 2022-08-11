from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        def simple_rob(nums):
            rob, not_rob = 0, 0
            for num in nums:
                # rob, means last time not rob + this time num
                # not rob, means we need to find the max between last time not rob or last time rob
                rob, not_rob = not_rob + num, max(rob, not_rob)
            return max(rob, not_rob)
        
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            return max(simple_rob(nums[1:]), simple_rob(nums[:-1]))

if __name__ == "__main__":
    nums = [2,3,2]
    assert 3 == Solution().rob(nums)

    nums = [1,2,3,1]
    assert 4 == Solution().rob(nums)

    nums = [1,2,3]
    assert 3 == Solution().rob(nums)