from collections import defaultdict
from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(check):
            return check == check[::-1]

        words = {word: i for i, word in enumerate(words)} # make a dict for all words and match their indices
        valid_pals = []
        for k, word in enumerate(list(words.keys())):
            n = len(word)
            for j in range(n+1):
                pref = word[:j]
                suf = word[j:]
                if is_palindrome(pref):
                    back = suf[::-1]
                    if back != word and back in words: # back == word, the word itself is a palindrome
                        valid_pals.append([words[back],  k])
                if j != n and is_palindrome(suf): # when j == n, array index out of bound
                    back = pref[::-1]
                    if back != word and back in words:
                        valid_pals.append([k, words[back]])
        return valid_pals
                

if __name__ == "__main__":
    words = ["abcd","dcba","lls","s","sssll"]
    print(Solution().palindromePairs(words))
    # Output: [[0,1],[1,0],[3,2],[2,4]]

    words = ["bat","tab","cat"]
    print(Solution().palindromePairs(words))
    # Output: [[0,1],[1,0]]

    words = ["a",""]
    print(Solution().palindromePairs(words))
    # Output: [[0,1],[1,0]]