from typing import List
def numberOfSubarrays(nums: List[int], k: int) -> int:
    current_counts = 0
    left_most_valid_index = -1
    odd_indices = []
    result = 0
    # i denote how many subarray includes index i
    # the number of possible arrays are those between last k odds and last k+1 odds
    # [1,2,2,1,1,1] for this case, when i = 5, left_most = 0, odd_indices = [3,4,5], so should be 3-0 = 3 results
    #                when i = 4, left_most = -1, odd_indices = [0,3,4], so should be 0-(-1) = 1 result 
    # [2,2,2,1,1,1] for this case, when i = 5, left_most = -1, odd_indices = [3,4,5], so should be 3-(-1) = 4 results
    for i, num in enumerate(nums):
        if num % 2 == 1:
            if current_counts < k:
                current_counts += 1
            else:
                left_most_valid_index = odd_indices.pop(0)
            odd_indices.append(i)
        if current_counts == k:
            result += odd_indices[0] - left_most_valid_index
    return result

nums = [1,1,2,1,1]
k = 3
print(numberOfSubarrays(nums, k))
# Output: 2

nums = [2,4,6]
k = 1
print(numberOfSubarrays(nums, k))
# Output: 0

nums = [2,2,2,1,2,2,1,2,2,2]
k = 2
print(numberOfSubarrays(nums, k))
# Output: 16