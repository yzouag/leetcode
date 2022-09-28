from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        best = 0
        for a in range(-m + 1, n):
            cur = 0
            for b in range(max(0, -a), min(n - a, m)):
                if nums1[a + b] == nums2[b]:
                    cur += 1
                    best = max(best, cur)
                else:
                    cur = 0
        return best

if __name__ == "__main__":
    nums1 = [1,2,3,2,1]
    nums2 = [3,2,1,4,7]
    assert 3 == Solution().findLength(nums1, nums2)

    nums1 = [0,0,0,0,0]
    nums2 = [0,0,0,0,0]
    assert 5 == Solution().findLength(nums1, nums2)