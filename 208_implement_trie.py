# where to use Trie?
# search a word in a dataset
# why not hash table? 
# if dataset is large, a lot of hash collision, worst as O(n)
# also, cannot support find keys with a common prefix
# enumerate a dataset of strings in lexicographical order
# Trie uses less space if lots of words in same prefix
# searching a key in a balanced tree node requires O(mlogn) time

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True


# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))   # return True
print(trie.search("app"))    # return False
print(trie.startsWith("app")) # return True
trie.insert("app")
print(trie.search("app"))     # return True