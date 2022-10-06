def wordPattern(pattern: str, s: str) -> bool:
    pattern_dict = {}
    s = s.split(" ")

    if len(s) != len(pattern):
        return False
    
    if len(set(pattern)) != len(set(s)):
        return False

    for i in range(len(s)):
        if pattern[i] not in pattern_dict:
            pattern_dict[pattern[i]] = s[i]
        else:
            if pattern_dict[pattern[i]] != s[i]:
                return False
    return True

pattern = "abba"
s = "dog cat cat dog"
assert wordPattern(pattern, s) == True

pattern = "abba"
s = "dog cat cat fish"
assert wordPattern(pattern, s) == False

pattern = "aaaa"
s = "dog cat cat dog"
assert wordPattern(pattern, s) == False
