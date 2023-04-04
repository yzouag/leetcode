def partitionString(s: str) -> int:
    res = 0
    
    chars = set()
    for ch in s:
        if ch in chars:
            chars = set([ch])
            res += 1
        else:
            chars.add(ch)
    
    if len(chars) > 0:
        res += 1
    
    return res

s = "abacaba"
print(partitionString(s))
# Output: 4

s = "ssssss"
print(partitionString(s))
# Output: 6