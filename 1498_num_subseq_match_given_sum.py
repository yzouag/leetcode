from typing import List

def numSubseq(nums: List[int], target: int) -> int:
    sorted_num = sorted(nums)

    # n = len(nums)
    # res = 0
    # for min_index in range(n):
    #     for max_index in range(min_index, n):
    #         if sorted_num[min_index] + sorted_num[max_index] > target:
    #             break
    #         if max_index - min_index <= 1:
    #             res += 1
    #         else:
    #             res += 2**(max_index-min_index-1)
    # return res % (10**9+7)

    res = 0
    l = 0
    r = len(sorted_num)-1
    while l < len(sorted_num):
        while sorted_num[l] + sorted_num[r] > target and r >= l:
            r -= 1
        if r < l:
            break
        res += 2**(r - l) # for min fixed at l, max can be anything between [l, r], there are total 2**(r-l) subsequences
        l += 1
    return res % (10**9+7) 

nums = [3,5,6,7]
target = 9
print(numSubseq(nums, target))
# Output: 4

nums = [3,3,6,8]
target = 10
print(numSubseq(nums, target))
# Output: 6

nums = [2,3,3,4,6,7]
target = 12
print(numSubseq(nums, target))
# Output: 61