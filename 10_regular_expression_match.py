class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # add empty character at the start to represent empty string and empty pattern
        # a none empty string does NOT match with any empty pattern, the first column is false
        # the empty string MAYBE match with a none empty pattern (if the pattern is a*)
        # the empty string must match with the empty pattern, so (0, 0) is true 
        s = ' ' + s
        p = ' ' + p
        len_s = len(s)
        len_p = len(p)

        # initialize the whole dp table
        dp = [[False] * len_p for i in range(len_s)]
        dp[0][0] = True

        # initialize the first row
        for j in range(1, len_p):
            if p[j] == '*':
                dp[0][j] = dp[0][j-2]

        for i in range(1, len_s):
            for j in range(1, len_p):
                # if string at position i matches with pattern at position j
                # we check if its previous string and pattern also matches
                if s[i] == p[j] or p[j] == '.':
                    dp[i][j] = dp[i-1][j-1]
                # sometimes, for pattern (xa*) with string (x), they match
                # so we need to check pattern(x), which is j-2, with string (x)
                # or for pattern (xa*) with string (xa), they match
                # in this case, pattern[j-1] is 'a', which matches xa's 'a'
                # we just check if xa matches xa
                elif p[j] == '*':
                    dp[i][j] = dp[i][j-2] or (dp[i-1][j] and (s[i]==p[j-1] or p[j-1] == '.'))
        return dp[-1][-1]

if __name__ == "__main__":   
    s = "aa"
    p = "a"
    assert False == Solution().isMatch(s, p)

    s = "aa"
    p = "a*"
    assert True == Solution().isMatch(s, p)

    s = "ab"
    p = ".*"
    assert True == Solution().isMatch(s, p)

    s = "xaabyc"
    p = "xa*b.c"
    assert True == Solution().isMatch(s, p)

    s = "aaa"
    p = "ab*a*c*a"
    assert True == Solution().isMatch(s, p)