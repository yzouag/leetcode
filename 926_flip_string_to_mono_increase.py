from collections import Counter
def minFlipsMonoIncr(s: str) -> int:
    # R = Counter(s)
    # L = {'0':0, '1': 0}
    # flips = [float('inf')] * (len(s)+1)
    # flips[0] = R['0']
    # flips[-1] = R['1']
    # for i in range(1, len(s)):
    #     L[s[i-1]] += 1
    #     R[s[i-1]] -= 1
    #     flips[i] = L['1'] + R['0']
    # return min(flips)

    # dp[i] = dp[i-1] (if s[i] == '1')
    #         min(dp[i-1]+1, num_of_1_before_i) (if s[i] == '0', flip this 0 to 1, or flip all number of 1 before to 0)
    ans = 0
    num = 0
    for c in s:
        if c == '0':
            ans = min(num, ans + 1)
        else:
            num += 1
    return ans
    # min_flip = float('inf')
    # for i in range(len(s)+1):
    #     flips = 0
    #     for index, w in enumerate(s):
    #         if index > i - 1: # on the right, all 1
    #             if w == '0': flips += 1
    #         else: # on the left, all 0
    #             if w == '1': flips += 1
    #     min_flip = min(flips, min_flip)
    # return min_flip

s = "00110"
print(minFlipsMonoIncr(s)) # Output: 1

s = "010110"
print(minFlipsMonoIncr(s)) # Output: 2

s = "00011000"
print(minFlipsMonoIncr(s)) # Output: 2

