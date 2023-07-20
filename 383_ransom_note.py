from collections import Counter
def canConstruct(ransomNote: str, magazine: str) -> bool:
    r = Counter(ransomNote)
    m = Counter(magazine)

    for k, v in r.items():
        if m[k] < v:
            return False
    return True

ransomNote = "a"
magazine = "b"
print(canConstruct(ransomNote, magazine))
# Output: false

ransomNote = "aa"
magazine = "ab"
print(canConstruct(ransomNote, magazine))
# Output: false

ransomNote = "aa"
magazine = "aab"
print(canConstruct(ransomNote, magazine))
# Output: true