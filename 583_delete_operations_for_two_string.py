def minDistance(word1: str, word2: str) -> int:
    # dp[i, j] is num delete for str1[:i], str2[:j]
    dp = [[0] * (1+len(word2)) for _ in range(1+len(word1))]
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if i == 0 or j == 0:
                dp[i][j] = i + j # need to delete all i or all j
            elif word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1] # the last character are the same, no need to delete
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1]) # not same, delete either word1 or word2's last char
    return dp[-1][-1]

word1 = "sea"
word2 = "eat"
print(minDistance(word1, word2))
# Output: 2

word1 = "leetcode"
word2 = "etco"
print(minDistance(word1, word2))
# Output: 4