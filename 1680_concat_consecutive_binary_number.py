class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = n
        M = (10**9+7)
        current_multiplier = 0
        temp = n
        while temp >= 1:
            temp = temp // 2
            current_multiplier += 1
        current_threshold = 1 << (current_multiplier-1)
        current_digits = current_multiplier

        for i in range(n-1, 0, -1):
            res += (i << current_digits) % M
            if i < current_threshold:
                current_multiplier -= 1
                current_threshold >>= 1
            current_digits += current_multiplier
        return res

if __name__ == "__main__":
    n = 1
    assert Solution().concatenatedBinary(n) == 1

    n = 3
    assert Solution().concatenatedBinary(n) == 27

    n = 4
    assert Solution().concatenatedBinary(n) == 220

    n = 12
    assert Solution().concatenatedBinary(n) == 505379714