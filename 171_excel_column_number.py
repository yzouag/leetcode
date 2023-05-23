def titleToNumber(columnTitle: str) -> int:
    res = 0
    for ch in columnTitle:
        res = res * 26 + (ord(ch) - ord("A") + 1)
    return res

columnTitle = "A"
print(titleToNumber(columnTitle))
# Output: 1

columnTitle = "AB"
print(titleToNumber(columnTitle))
# Output: 28

columnTitle = "ZY"
print(titleToNumber(columnTitle))
# Output: 701