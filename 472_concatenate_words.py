from typing import List
def findAllConcatenatedWordsInADict(words: List[str]) -> List[str]:
    all_words = set(words)
    res = []
    for word in words:
        all_words.remove(word)
        dp = [False] * (len(word) + 1)
        dp[0] = True
        # dp[i] = dp[j] && word[j, i] in dictionary
        for i in range(1, len(dp)):
            for j in range(i):
                if dp[j] and (word[j:i] in all_words):
                    dp[i] = True
                    break
        if dp[-1] == True:
            res.append(word)
        all_words.add(word)
    return res
    

words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print(findAllConcatenatedWordsInADict(words))
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

words = ["cat","dog","catdog"]
print(findAllConcatenatedWordsInADict(words))
# Output: ["catdog"]