from typing import List
import string

def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    wordList = set(wordList)
    queue = [beginWord]
    step = 1
    while queue:
        temp = []
        for word in queue:
            if word == endWord:
                return step
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    neighbor_word = word[:i] + c + word[i+1:]
                    if neighbor_word in wordList:
                        temp.append(neighbor_word)
                        wordList.remove(neighbor_word)
        step += 1
        queue = temp
    return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(ladderLength(beginWord, endWord, wordList))
# Output: 5

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
print(ladderLength(beginWord, endWord, wordList))
# Output: 0