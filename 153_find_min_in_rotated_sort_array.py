from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        # no rotation
        if nums[0] <= nums[-1]:
            return nums[0]
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= nums[0]:
                l = mid + 1
            # elif nums[mid] < nums[mid+1] and nums[mid] < nums[mid-1]:
            #     return mid
            else:
                r = mid - 1
        return nums[l]

if __name__ == "__main__":
    nums = [3,4,5,1,2]
    assert Solution().findMin(nums) == 1
    
    nums = [4,5,6,7,0,1,2]
    assert Solution().findMin(nums) == 0

    nums = [11,13,15,17]
    assert Solution().findMin(nums) == 11

    nums = [1]
    assert Solution().findMin(nums) == 1

    nums = [2, 1]
    assert Solution().findMin(nums) == 1
