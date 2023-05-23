def romanToInt(s: str) -> int:
    value_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    res = 0
    for i, ch in enumerate(s):
        if i < len(s)-1 and value_dict[s[i+1]] > value_dict[ch]:
            res -= value_dict[ch]
        else:
            res += value_dict[ch]
    return res

s = "III"
print(romanToInt(s))
# Output: 3

s = "LVIII"
print(romanToInt(s))
# Output: 58

s = "MCMXCIV"
print(romanToInt(s))
# Output: 1994