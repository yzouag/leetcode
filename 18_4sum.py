from typing import List

from numpy import average


class Solution:
    # here it uses the recursion
    # for n sum question, it will finally die down to 2 sum question, the base case
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums : List[int], target: int, k:int) -> List[List[int]]:
            res = []
            # no enough number
            if len(nums) < k:
                return res
            
            # if the smallest number is larger than average, or the largest number is smaller than average
            # the nums must exceed the target
            average_val = target // k
            if average_val > nums[-1] or average_val < nums[0]:
                return res
            
            if k == 2:
                return twoSum(nums, target)
            
            for i in range(len(nums)):
                # if nums[i] is same as nums[i-1], then they will have the same result
                if i == 0 or nums[i-1] != nums[i]:
                    for subset in kSum(nums[i+1:], target - nums[i], k-1):
                        res.append(subset + [nums[i]]) # list + list will resturn a copy of list concat
                    
            return res

        def twoSum(nums : List[int], target: int) -> List[List[int]]:
            res = []
            lo, hi = 0, len(nums)-1
            while lo < hi:
                current_sum = nums[lo] + nums[hi]
                # if current sum is smaller, left pointer goes up
                # if the number are the same, then skip it
                if current_sum < target or (lo > 0 and nums[lo] == nums[lo-1]):
                    lo += 1
                elif current_sum > target or (hi < len(nums)-1 and nums[hi] == nums[hi+1]):
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
            return res
        
        nums.sort()
        return kSum(nums, target, 4)

        

if __name__ == "__main__":
    nums = [1,0,-1,0,-2,2]
    target = 0
    # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    print(Solution().fourSum(nums, target))

    nums = [2,2,2,2,2]
    target = 8
    # [[2,2,2,2]]
    print(Solution().fourSum(nums, target))
 