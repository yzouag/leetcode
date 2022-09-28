from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # denote a[i] as the longest increasing subsequence which must include nums[i]
        # a[0] = (1, nums[0]) -> (lengthOfLIS, max_of_LIS)
        # a[i] is max of a[0] to a[i-1] with max_of_LIS < nums[i]
        
        best_result = 1
        n = len(nums)
        length_of_LIS = [0] * n
        
        length_of_LIS[0] = 1
        for i in range(1, len(nums)):
            current_max_length = 0
            for j in range(0, i):
                if nums[j] < nums[i] and current_max_length < length_of_LIS[j]:
                    current_max_length = length_of_LIS[j]
            length_of_LIS[i] = current_max_length + 1
            if best_result < length_of_LIS[i]:
                best_result = length_of_LIS[i]
        return best_result

if __name__ == "__main__":
    nums = [10,9,2,5,3,7,101,18]
    assert Solution().lengthOfLIS(nums) == 4

    nums = [0,1,0,3,2,3]
    assert Solution().lengthOfLIS(nums) == 4

    nums = [7,7,7,7,7,7,7]
    assert Solution().lengthOfLIS(nums) == 1