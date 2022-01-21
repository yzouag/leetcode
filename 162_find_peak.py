from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[mid+1]:
                l = mid + 1
            else:
                r = mid
        return l
                

if __name__ == "__main__":
    nums = [1,2,3,1]
    assert Solution().findPeakElement(nums) == 2

    nums = [1,2,1,3,5,6,4]
    assert Solution().findPeakElement(nums) in [5, 1]

