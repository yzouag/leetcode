def longestPalindrome(s: str) -> str:
    N = len(s)
    longest = 0
    res = ''

    for i in range(2*N-1):
        length = 0
        left = i // 2
        right = (i+1) // 2
        while left >= 0 and right < N and s[left] == s[right]:
            if left == right: length += 1
            else: length += 2
            left -= 1
            right += 1
        if length > longest:
            longest = length
            res = s[left+1:right]
    return res

if __name__ == "__main__":
    s = "babad"
    print(longestPalindrome(s))
    assert 'bab' == longestPalindrome(s)

    s = "cbbd"
    print(longestPalindrome(s))
    assert 'bb' == longestPalindrome(s)