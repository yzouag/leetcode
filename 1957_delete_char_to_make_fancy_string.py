def makeFancyString(s: str) -> str:
    res = s[0]
    prev = s[0]
    count = 1
    for ch in s[1:]:
        if ch == prev:
            count += 1
            if count < 3:
                res += ch
        else:
            prev = ch
            count = 1
            res += ch
    return res

s = "leeetcode"
print(makeFancyString(s))
# Output: "leetcode"

s = "aaabaaaa"
print(makeFancyString(s))
# Output: "aabaa"

s = "aab"
print(makeFancyString(s))
# Output: "aab"