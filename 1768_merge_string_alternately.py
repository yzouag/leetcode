def mergeAlternately(word1: str, word2: str) -> str:
    i = 0
    res = ""
    while i < len(word1) and i < len(word2):
        res += word1[i] + word2[i]
        i += 1
    res += word1[i:] + word2[i:]
    return res

word1 = "abc"
word2 = "pqr"
print(mergeAlternately(word1, word2))
# Output: "apbqcr"

word1 = "ab"
word2 = "pqrs"
print(mergeAlternately(word1, word2))
# Output: "apbqrs"

word1 = "abcd"
word2 = "pq"
print(mergeAlternately(word1, word2))
# Output: "apbqcd"