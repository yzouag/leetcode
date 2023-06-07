# from typing import List, Set, Tuple
from typing import List
from functools import reduce
from collections import defaultdict
# class TrieNode:
#     def __init__(self) -> None:
#         self.children  = {}
#         self.isEnd = False

def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    # build the trie
    # root = TrieNode()
    # for word in words:
    #     node = root
    #     for ch in word:
    #         if ch not in node.children:
    #             node.children[ch] = TrieNode()
    #         node = node.children[ch]
    #     node.isEnd = True

    # m = len(board)
    # n = len(board[0])
    # res = set()
    # def dfs(i: int, j: int, node: TrieNode, visited: Set[Tuple[int, int]], word: str):
    #     if (i, j) in visited:
    #         return
    #     if i < 0 or i >= m or j < 0 or j >= n:
    #         return
    #     if board[i][j] not in node.children:
    #         return
    #     word = word+board[i][j]
    #     node = node.children[board[i][j]]
    #     if node.isEnd:
    #         res.add(word)
    #     visited.add((i, j))
    #     dfs(i-1, j, node, visited, word)
    #     dfs(i+1, j, node, visited, word)
    #     dfs(i, j-1, node, visited, word)
    #     dfs(i, j+1, node, visited, word)
    #     visited.remove((i, j))

    # # scan through whole graph
    # for i in range(m):
    #     for j in range(n):
    #         visited = set()
    #         dfs(i, j, root, visited, "")
    
    # return list(res)
    # create trie
    Trie = lambda: defaultdict(Trie)
    trie = Trie()
    END = True
    
    for word in words:
        reduce(dict.__getitem__,word,trie)[END] = word
    
    res = set()
    def findstr(i,j,t):
        if END in t:
            res.add(t[END])
            # return
        letter = board[i][j]
        board[i][j] = ""
        if i > 0 and board[i-1][j] in t:
            findstr(i-1,j,t[board[i-1][j]])
        if j>0 and board[i][j-1] in t:
            findstr(i,j-1,t[board[i][j-1]])
        if i < len(board)-1 and board[i+1][j] in t:
            findstr(i+1,j,t[board[i+1][j]])
        if j < len(board[0])-1 and board[i][j+1] in t:
            findstr(i,j+1,t[board[i][j+1]])
        board[i][j] = letter
        
        return 
    
    for i, row in enumerate(board):
        for j, char in enumerate(row):
            if board[i][j] in trie:
                findstr(i,j,trie[board[i][j]])
    return res

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
print(findWords(board, words))
# Output: ["eat","oath"]

board = [["a","b"],["c","d"]]
words = ["abcb"]
print(findWords(board, words))
# Output: []

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain","hklf", "hf"]
print(findWords(board, words))
# Output: ['hklf', 'eat', 'hf', 'oath']