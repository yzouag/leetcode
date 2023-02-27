# base case:
# word1 = "", return len(word2) (or another way around)
# recursive relation:
# if word1[0] == word2[0]:
#   no operation needed, proceed to word1[1:], word2[1:]
# else:
#   1. insert in word1: dp(word1, word2) = 1 + dp(word1, word2[1:])
#       now word1 add a prefix letter which is same as word2[0], then compare remaining letters of word2
#   2. delete in word1: dp(word1, word2) = 1 + dp(word1[1:], word2)
#       similar idea as 1
#   3. replace in word1: dp(word1, word2) = 1 + dp(word1[1:], word2[1:])
#       replace the first letter of word1 to the same as word2, and then proceed to both of their remaining letters
#   the result should be min(insert, delete, repalce)

def minDistance(word1: str, word2: str) -> int:
    # # top down approach
    # # a lot of repetitions, when we calculate dp(word1[i:], word2[j:]) again and again
    memo = {}
    def dp(word1, word2) -> int:
        # base case:
        i, j = len(word1), len(word2)
        if i == 0:
            memo[(i,j)] = j
            return j
        if j == 0:
            memo[(i,j)] = i
            return i
    
        # iterations
        if (i, j) not in memo:
            if word1[0] == word2[0]:
                memo[(i,j)] = dp(word1[1:], word2[1:])
            else:
                insert = 1 + dp(word1[1:], word2)
                delete = 1 + dp(word1, word2[1:])
                repalce = 1 + dp(word1[1:], word2[1:])
                memo[(i,j)] = min([insert, delete, repalce])
        return memo[(i, j)]
    return dp(word1, word2)



word1 = "horse"
word2 = "ros"
print(minDistance(word1, word2))
# Output: 3

word1 = "intention"
word2 = "execution"
print(minDistance(word1, word2))
# Output: 5