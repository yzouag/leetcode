# key observation:
# if one word of maxSize appear n time, all its substring also appear at least n times
# so we only need to consider minSize
from collections import Counter

def maxFreq(s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
    count = Counter(s[i:i + minSize] for i in range(len(s) - minSize + 1))
    return max([count[w] for w in count if len(set(w)) <= maxLetters] + [0])


s = "aababcaab"
maxLetters = 2
minSize = 3
maxSize = 4
print(maxFreq(s, maxLetters, minSize, maxSize)) # 2

s = "aaaa"
maxLetters = 1
minSize = 3
maxSize = 3
print(maxFreq(s, maxLetters, minSize, maxSize)) # 2
