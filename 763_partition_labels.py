from typing import List
from collections import Counter

def partitionLabels(s: str) -> List[int]:
    # letter_counter = Counter(s)
    # res = []
    # letter_in_group = set()
    # counts = 0
    # for letter in s:
    #     counts += 1
    #     letter_counter[letter] -= 1
    #     letter_in_group.add(letter)
    #     if letter_counter[letter] == 0:
    #         letter_in_group.remove(letter)
    #         if len(letter_in_group) == 0:
    #             res.append(counts)
    #             counts = 0
    # return res

    # smarter solution
    # first record the last occurence of each letter
    # walk from current letter to its last occurence index
    # if no new word encountered, or the new word has its last occurence before current last index
    # get the result
    # else, update the last index to the new word's last occurence index
    L = len(s)
    last = {s[i]: i for i in range(L)} # last appearance of the letter
    i, ans = 0, []
    while i < L:
        end, j = last[s[i]], i + 1
        while j < end: # validation of the part [i, end]
            if last[s[j]] > end:
                end = last[s[j]] # extend the part
            j += 1
        
        ans.append(end - i + 1)
        i = end + 1
        
    return ans

s = "ababcbacadefegdehijhklij"
print(partitionLabels(s))
# Output: [9,7,8]

s = "eccbbbbdec"
print(partitionLabels(s))
# Output: [10]