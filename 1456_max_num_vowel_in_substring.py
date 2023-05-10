def maxVowels(s: str, k: int) -> int:
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    num_vowels = 0
    for i in range(k):
        if s[i] in vowels:
            num_vowels += 1
    result = num_vowels

    for i in range(k, len(s)):
        if s[i] in vowels:
            num_vowels += 1
        if s[i-k] in vowels:
            num_vowels -= 1
        if num_vowels > result:
            result = num_vowels
    return result

s = "abciiidef"
k = 3
print(maxVowels(s, k))
# Output: 3

s = "aeiou"
k = 2
print(maxVowels(s, k))
# Output: 2

s = "leetcode"
k = 3
print(maxVowels(s, k))
# Output: 2

s = "ibpbhixfiouhdljnjfflpapptrxgcomvnb"
k = 33
print(maxVowels(s, k))
# Output: 7