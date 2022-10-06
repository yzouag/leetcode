from collections import defaultdict
from typing import List
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    res = []
    anagram_group = defaultdict(list)
    for word in strs:
        word_list = list(word)
        word_list.sort()
        word_repr = "".join(word_list)
        anagram_group[word_repr].append(word)
    for key in anagram_group:
        res.append(anagram_group[key])
    return res

    # key takeaway: tuple is hashable, in fact, all immutable objects should be hashable
    # this method is a bit slower
    # letters_to_words = defaultdict(list)
    # for word in strs:
    #     letters_to_words[tuple(sorted(word))].append(word)
    # return list(letters_to_words.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

strs = [""]
print(groupAnagrams(strs))
# Output: [[""]]

strs = ["a"]
print(groupAnagrams(strs))
# Output: [["a"]]