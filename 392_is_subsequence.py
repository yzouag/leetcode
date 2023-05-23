def isSubsequence(s: str, t: str) -> bool:
    if len(s) == 0:
        return True
    i, j = 0, 0
    while j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
            if i == len(s):
                return True
        else:
            j += 1
    return False

s = "abc"
t = "ahbgdc"
print(isSubsequence(s, t))
# Output: true

s = "axc"
t = "ahbgdc"
print(isSubsequence(s, t))
# Output: false

s = "acb"
t = "ahbgdc"
print(isSubsequence(s, t))
# Output: false