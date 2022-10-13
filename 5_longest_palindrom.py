class Solution:
    def longestPalindrome(self, s: str) -> str:
        # method 1: expand around the center
        # if not s:
        #     return ""
        
        # def expand(left, right):
        #     while left >= 0 and right < len(s)-1 and s[left] == s[right]:
        #         left -= 1
        #         right += 1
        #     return left, right
        
        # maxlen = 0
        # for i in range(len(s)):
        #     l1, r1 = expand(i, i)
        #     l2, r2 = expand(i, i+1)
        #     if (r1 - l1) > (r2 - l2) and (r1 - l1 + 1) > maxlen:
        #         start, end, maxlen = l1, r1, (r1 -l1 +1)
        #     if (r1 - l1) > (r2 - l2) and (r1 - l1 + 1) > maxlen:
        #         start, end, maxlen = l1, r1, (r1 -l1 +1)
        # return s[start:end+1]

        # dynamic programming
        # denote a[i][j] as the 

if __name__ == "__main__":
    s = "babad"
    print(Solution().longestPalindrome(s))
    assert 'bab' == Solution().longestPalindrome(s)

    s = "cbbd"
    assert 'bb' == Solution().longestPalindrome(s)