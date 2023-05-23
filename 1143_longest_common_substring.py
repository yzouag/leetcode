def longestCommonSubsequence(text1: str, text2: str) -> int:
    n1, n2 = len(text1), len(text2)
    memo = {}
    def dfs(i, j):
        if i == n1 or j == n2:
            return 0
        if (i, j) in memo:
            return memo[(i,j)]
        
        if text1[i] == text2[j]:
            memo[(i,j)] = 1 + dfs(i+1, j+1)
        else:
            memo[(i,j)] = max(dfs(i+1, j), dfs(i, j+1))
        return memo[(i,j)]
    return dfs(0, 0)

text1 = "abcde"
text2 = "ace"
print(longestCommonSubsequence(text1, text2)) 
# Output: 3

text1 = "abc"
text2 = "abc"
print(longestCommonSubsequence(text1, text2)) 
# Output: 3

text1 = "abc"
text2 = "def"
print(longestCommonSubsequence(text1, text2)) 
# Output: 0