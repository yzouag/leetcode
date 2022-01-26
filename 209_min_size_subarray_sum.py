from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, num_sum, count = 0, 0, 999999
        for right in range(len(nums)):
            num_sum += nums[right]
            while num_sum >= target and left <= right:
                if right - left + 1 < count:
                    count = right - left + 1
                num_sum -= nums[left]
                left += 1
        return count if count != 999999 else 0

if __name__ == "__main__":
    target = 7
    nums = [2,3,1,2,4,3]
    assert 2 == Solution().minSubArrayLen(target, nums)

    target = 4
    nums = [1,4,4]
    assert 1 == Solution().minSubArrayLen(target, nums)

    target = 11
    nums = [1,1,1,1,1,1,1,1]
    assert 0 == Solution().minSubArrayLen(target, nums)