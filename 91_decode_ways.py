def numDecodings(s: str) -> int:
    if s[0] == '0':
        return 0
    prev2, prev1 = 1, 1
    for i in range(1, len(s)):
        if s[i] == '0':
            if s[i-1] == '1' or s[i-1] == '2':
                tmp = prev2
            else:
                return 0
        elif int(s[i-1:i+1]) <= 26 and s[i-1] != '0':
                tmp = prev1 + prev2
        else:
            tmp = prev1
        prev2 = prev1
        prev1 = tmp
    return prev1

s = "12"
print(numDecodings(s))
# Output: 2

s = "226"
print(numDecodings(s))
# Output: 3

s = "06"
print(numDecodings(s))
# Output: 0


s = "1123"
print(numDecodings(s))
# Output: 5