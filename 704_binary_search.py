from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # standard answer:
        left, right = 0, len(nums)-1
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] == target:
                return pivot
            elif target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1
        # MY IMPLEMENTATION:  TOOOOOOOOOOOOOOOOOO SLOW!
        # def binary_search(target, start, end):
        #     if end - start <= 1:
        #         if target == nums[start]:
        #             return start
        #         elif target == nums[end]:
        #             return end
        #         else:
        #             return -1
        #     mid = (start + end) // 2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         return binary_search(target, mid, end)
        #     else:
        #         return binary_search(target, start, mid)
        
        # return binary_search(target, 0, len(nums)-1)
    
if __name__ == '__main__':
    nums = [-1,0,3,5,9,12]
    target = 2
    a = Solution()
    print(a.search(nums, target))