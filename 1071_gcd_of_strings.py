def gcdOfStrings(str1: str, str2: str) -> str:
    l1 = len(str1)
    l2 = len(str2)
    for i in range(min(l1,l2), 0, -1):
        if l1 % i == 0 and l2 % i == 0:
            substring = str1[:i]
            if ((l1 + l2)//i) * substring == (str1 + str2):
                return substring
    return ''

str1 = "ABCABC"
str2 = "ABC"
print(gcdOfStrings(str1, str2))
# Output: "ABC"

str1 = "ABABAB"
str2 = "ABAB"
print(gcdOfStrings(str1, str2))
# Output: "AB"

str1 = "LEET"
str2 = "CODE"
print(gcdOfStrings(str1, str2))
# Output: ""