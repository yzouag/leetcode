from typing import List



class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Idea / Proof:
        1. The widest container (using first and last line) is a good candidate, because of its width. Its water level is the height of the smaller one of first and last line.
        2. All other containers are less wide and thus would need a higher water level in order to hold more water.
        3. The smaller one of first and last line doesn't support a higher water level and can thus be safely removed from further consideration.
        """
        i, j = 0, len(height)-1
        res = -1
        while i < j:
            area = min(height[i], height[j]) * (j - i)
            if res < area:
                res = area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res

if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    assert 49 == Solution().maxArea(height)

    height = [1,1]
    assert 1 == Solution().maxArea(height)
