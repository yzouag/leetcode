from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pos = len(digits)-1
        while digits[pos] == 9:
            digits[pos] = 0
            pos -= 1
            if pos == -1:
                digits.insert(0, 1)
                return digits
        digits[pos] += 1
        return digits
        

if __name__ == "__main__":
    digits = [1,2,3]
    assert [1,2,4] == Solution().plusOne(digits)

    digits = [4,3,2,1]
    assert [4,3,2,2] == Solution().plusOne(digits)

    digits = [9]
    assert [1,0] == Solution().plusOne(digits)