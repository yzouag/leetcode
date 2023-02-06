from typing import List

def isAlienSorted(words: List[str], order: str) -> bool:
    if len(words) <= 1:
        return True
    
    alph_order = {}
    for i in range(26):
        alph_order[order[i]] = i

    def not_in_order(x: str, y: str):
        for i in range(min(len(x), len(y))):
            if alph_order[x[i]] > alph_order[y[i]]:
                return True
            elif alph_order[x[i]] < alph_order[y[i]]:
                return False
        if len(x) > len(y):
            return True
        return False

    for i in range(1, len(words)):
        if not_in_order(words[i-1], words[i]):
            return False
    return True

words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(isAlienSorted(words, order))
# true

words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"
print(isAlienSorted(words, order))
# false

words = ["apple","app"]
order = "abcdefghijklmnopqrstuvwxyz"
print(isAlienSorted(words, order))
# false