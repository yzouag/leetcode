from typing import List


def wordBreak(s: str, wordDict: List[str]) -> bool:
    # method 1: dp, and loop from dp list
    word_set = set(wordDict)
    # dp[i] = or(dp[i-1], s[i:i+1] in dict)
    dp = [False] * (len(s)+1)
    dp[0] = True
    for i in range(1, len(s)+1):
        for j in range(i):
            if dp[j] and (s[j:i] in word_set):
                dp[i] = True
                continue
    return dp[-1]

    # # method 2: dp, but loop from the wordDict
    # dp = [False] * len(s)
    # for i in range(len(s)):
    #     for word in wordDict:
    #         if s[i-len(word)+1:i+1] == word and (dp[i-len(word)] or (i-len(word) == -1)):
    #             dp[i] = True
    # return dp[-1]

s = "leetcode"
wordDict = ["leet","code"]
print(wordBreak(s, wordDict))
# Output: true

s = "applepenapple"
wordDict = ["apple","pen"]
print(wordBreak(s, wordDict))
# Output: true

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
print(wordBreak(s, wordDict))
# Output: false