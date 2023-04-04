class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        def helper(i: int, node: TrieNode) -> bool:
            if i == len(word):
                return node.isEnd

            if word[i] == '.':
                for ch in node.children:
                    if helper(i+1, node.children[ch]):
                        return True
                return False
            
            if word[i] in node.children:
                return helper(i+1, node.children[word[i]])
            return False
        return helper(0, self.root)


wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad"))  # return False
print(wordDictionary.search("bad"))  # return True
print(wordDictionary.search(".ad"))  # return True
print(wordDictionary.search("b.."))  # return True