from collections import defaultdict
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_dictionary = defaultdict(int)
        result = 0
        repeat_word = 0
        for word in words:
            if word[0] == word[1]:
                if word_dictionary[word] > 0:
                    word_dictionary[word] -= 1
                    repeat_word -= 1
                    result += 4
                else:
                    word_dictionary[word] += 1
                    repeat_word += 1
            else:
                if word_dictionary[word[::-1]] > 0:
                    result += 4
                    word_dictionary[word[::-1]] -= 1
                else:
                    word_dictionary[word] += 1
        if repeat_word > 0:
            result += 2
        return result



if __name__ == "__main__":
    words = ["lc","cl","gg"]
    assert Solution().longestPalindrome(words) == 6

    words = ["ab","ty","yt","lc","cl","ab"]
    assert Solution().longestPalindrome(words) == 8

    words = ["cc","ll","xx"]
    assert Solution().longestPalindrome(words) == 2