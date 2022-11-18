def reverseVowels(s: str) -> str:
    s = list(s)
    l, r = 0, len(s)-1
    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    while l < r:
        if s[l] in vowels and s[r] in vowels:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        if s[l] not in vowels:
            l += 1
        if s[r] not in vowels:
            r -= 1
    return "".join(s)

s = "hello"
print(reverseVowels(s))
# Output: "holle"

s = "leetcode"
print(reverseVowels(s))
# Output: "leotcede"