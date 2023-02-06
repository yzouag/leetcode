from typing import List

def removeAnagrams(words: List[str]) -> List[str]:
    if len(words) <= 1:
        return words

    res = []
    
    current_dict = [0] * 26
    current_word = words[0]
    for c in words[0]:
        current_dict[ord(c)-ord('a')] += 1
    
    for i in range(len(words)-1):
        t = words[i+1]
        
        if len(current_word) != len(t):
            res.append(current_word)
            current_dict = [0] * 26
            current_word = t
            for c in t:
                current_dict[ord(c)-ord('a')] += 1
            continue
        
        next_dict = [0]*26
        for c in t:
            next_dict[ord(c)-ord('a')] += 1
        if next_dict != current_dict:
            res.append(current_word)
            current_word = t
            current_dict = next_dict
    res.append(current_word)
    return res


words = ["abba","baba","bbaa","cd","cd"]
print(removeAnagrams(words))
# Output: ["abba","cd"]

words = ["a","b","c","d","e"]
print(removeAnagrams(words))
# Output: ["a","b","c","d","e"]