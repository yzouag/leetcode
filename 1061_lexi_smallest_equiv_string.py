import string


def smallestEquivalentString(s1: str, s2: str, baseStr: str) -> str:
    unions = {letter: letter for letter in string.ascii_lowercase}

    def find(l):
        if unions[l] != l:
            return find(unions[l])
        return l

    def connect(a, b):
        a = find(a)
        b = find(b)
        if a > b:
            unions[a] = b
        else:
            unions[b] = a
    
    for i in range(len(s1)):
        connect(s1[i], s2[i])

    res = ''
    for letter in baseStr:
        res += find(letter)
    return res

s1 = "parker"
s2 = "morris"
baseStr = "parser"
print(smallestEquivalentString(s1, s2, baseStr)) # "makkek"

s1 = "hello"
s2 = "world"
baseStr = "hold"
print(smallestEquivalentString(s1, s2, baseStr)) # "hdld"

s1 = "leetcode"
s2 = "programs"
baseStr = "sourcecode"
print(smallestEquivalentString(s1, s2, baseStr)) # "aauaaaaada"