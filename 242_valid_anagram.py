def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    char_s = [0] * 26
    for c in s:
        char_s[ord(c)-ord('a')] += 1
    for c in t:
        char_s[ord(c)-ord('a')] -= 1
        if char_s[ord(c)-ord('a')] < 0:
            return False
    return True


s = "anagram"
t = "nagaram"
print(isAnagram(s, t))
# Output: true

s = "rat"
t = "car"
print(isAnagram(s, t))
# Output: false