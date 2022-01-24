from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        res = []
        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: # for array like [0, 1, 1, 2, 4, ... ] two '1' will yield same result, so skip others
                continue
            target = 0 - nums[i]
            l, r = i+1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]: # similar, skip the duplicates
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[l]+nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return res


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(nums))  # Output: [[-1,-1,2],[-1,0,1]]
