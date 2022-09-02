from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        pass

if __name__ == "__main__":
    num = [1,2,0,0]
    k = 34
    assert [1,2,3,4] == Solution().addToArrayForm(num, k)

    num = [2,7,4]
    k = 181
    assert [4,5,5] == Solution().addToArrayForm(num, k)

    num = [2,1,5]
    k = 806
    assert [1,0,2,1] == Solution().addToArrayForm(num, k)