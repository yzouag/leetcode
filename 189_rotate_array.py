from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse_subarray(num_array, start, end):
            while start <= end:
                temp = num_array[end]
                num_array[end] = num_array[start]
                num_array[start] = temp
                start += 1
                end -= 1
        k = k % len(nums)
        nums.reverse()
        reverse_subarray(nums, 0, k-1)
        reverse_subarray(nums, k, len(nums)-1)
        return nums
        

if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3
    print(Solution().rotate(nums, k))