from collections import Counter

def closeStrings(word1: str, word2: str) -> bool:
    # never close for two different length words
    if len(word1) != len(word2):
        return False
    
    c1 = Counter(word1)
    c2 = Counter(word2)

    for key in c1.keys():
        if key not in c2.keys():
            return False

    l1 = sorted(c1.values())
    l2 = sorted(c2.values())

    return l1 == l2

word1 = "abc"
word2 = "bca"
print(closeStrings(word1, word2))
# Output: true

word1 = "a"
word2 = "aa"
print(closeStrings(word1, word2))
# Output: false

word1 = "cabbba" # 3b 2a 1c
word2 = "abbccc" # 3c 2b 1a
print(closeStrings(word1, word2))
# Output: true