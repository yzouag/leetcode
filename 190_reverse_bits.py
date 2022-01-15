class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans = (ans << 1) + (n & 1)
            n >>= 1
        return ans

if __name__ == "__main__":
    n = 11111111111111111111111111111101
    assert 3221225471 == Solution().reverseBits(n)