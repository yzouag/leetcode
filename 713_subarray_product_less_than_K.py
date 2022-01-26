from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left, prod, count = 0, 1, 0
        for right in range(len(nums)):
            prod *= nums[right]

            while prod >= k and left <= right:
                prod /= nums[left]
                left += 1
            count += right - left + 1
            """
            left and right form the sliding window. for each step we add the length of this window i.e., right - left + 1 to our counter.
            
            To illustrate,
                let window length be 2. When a new element comes into this window, we can form 3 subarrays with the new element.
                a, b --> window
                a, b, c --> new window
                [c], [b, c], [a, b, c] these are the new subarrays. Thus incrementing the counter with window length
            """
        return count

if __name__ == "__main__":
    nums = [10,5,2,6]
    k = 100
    assert 8 == Solution().numSubarrayProductLessThanK(nums, k)

    nums = [1,2,3]
    k = 0
    assert 0 == Solution().numSubarrayProductLessThanK(nums, k)
