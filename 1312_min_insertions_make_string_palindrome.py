# key observation:
# for any string s1 + palin_s + s2 + palin_s + s3
# the min insertions is to add s1, s2, s3 so that the whole string is palindromic
# the result should be len(s) - len(longest_palindromic_subsequence)

def minInsertions(s: str) -> int:
    memo = {}

    def longest_sub_palindrome(i, j):
        if i > j:
            return 0
        if i == j:
            return 1
        
        if (i, j) in memo:
            return memo[(i,j)]
        
        if s[i] == s[j]:
            memo[(i,j)] = 2 + longest_sub_palindrome(i+1, j-1)
        else:
            memo[(i,j)] = max(longest_sub_palindrome(i+1, j), longest_sub_palindrome(i, j-1))

        return memo[(i,j)]

    return len(s) - longest_sub_palindrome(0, len(s)-1)

s = "zzazz"
print(minInsertions(s))
# Output: 0

s = "mbadm"
print(minInsertions(s))
# Output: 2

s = "leetcode"
print(minInsertions(s))
# Output: 5