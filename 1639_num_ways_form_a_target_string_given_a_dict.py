from typing import List

def numWays(words: List[str], target: str) -> int:
    dict_length = len(words[0])
    num_dics = len(words)
    if dict_length < len(target):
        return 0
    
    freq = [[0]*26 for _ in range(dict_length)]
    for i in range(dict_length):
        for j in range(num_dics):
            freq[i][ord(words[j][i])-ord('a')] += 1
    
    memo = {}
    def dfs(i, target):
        if dict_length-i < len(target): # base case
            return 0
        if i == dict_length-1:
            return freq[i][ord(target[0])-ord('a')]
        
        if (i, target) in memo:
            return memo[(i, target)]
        
        if len(target) == 1:
            res = freq[i][ord(target[0])-ord('a')] + dfs(i+1, target)
        else:
            res = freq[i][ord(target[0])-ord('a')] * dfs(i+1, target[1:]) + dfs(i+1, target)
        memo[(i, target)] = res
        return res
    
    return dfs(0, target)%(10**9+7)

words = ["acca","bbbb","caca"]
target = "aba"
print(numWays(words, target))
# Output: 6

words = ["abba","baab"]
target = "bab"
print(numWays(words, target))
# Output: 4