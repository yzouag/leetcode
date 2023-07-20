def largestVariance(s: str) -> int:
    # O(n^2) solution using sliding window
    counter = [0] * 26
    res = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            
    return res

s = "aababbb"
print(largestVariance(s))
# Output: 3

s = "abcde"
print(largestVariance(s))
# Output: 0
