from typing import List

# using xor, two xor will return original number
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res

if __name__ == "__main__":
    nums = [4,1,2,1,2]
    assert 4 == Solution().singleNumber(nums)