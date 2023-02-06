from typing import List

def wordBreak(s: str, wordDict: List[str]) -> List[str]:
    pass

s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
print(wordBreak(s, wordDict))
# Output: ["cats and dog","cat sand dog"]


s = "pineapplepenapple"
wordDict = ["apple","pen","applepen","pine","pineapple"]
print(wordBreak(s, wordDict))
# Output: ["cats and dog","cat sand dog"]

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
print(wordBreak(s, wordDict))
# Output: ["cats and dog","cat sand dog"]