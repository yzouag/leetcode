from typing import List

def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    a1 = list(set(nums1).difference(nums2))
    a2 = list(set(nums2).difference(nums1))
    return [a1, a2]
    

nums1 = [1,2,3]
nums2 = [2,4,6]
print(findDifference(nums1, nums2))
# Output: [[1,3],[4,6]]

nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
print(findDifference(nums1, nums2))
# Output: [[3],[]]