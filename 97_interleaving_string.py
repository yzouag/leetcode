def isInterleave(s1: str, s2: str, s3: str) -> bool:
    m, n, s = len(s1), len(s2), len(s3)
    if s != m + n:
        return False
    
    seen = {}
    def dp(i: int, j: int) -> bool:
        # base case
        if i == m:
            if s3[i+j-s:] == s2[j:]:
                return True
            else:
                return False
        if j == n:
            if s3[i+j-s:] == s1[i:]:
                return True
            else:
                return False

        if (i, j) in seen:
            return seen[(i,j)]
        
        interleavable = False
        if s3[i+j] == s1[i]:
            interleavable |= dp(i+1, j)
        if s3[i+j] == s2[j]:
            interleavable |= dp(i, j+1)
        seen[(i,j)] = interleavable
        return interleavable
    
    return dp(0, 0)

s1 = ""
s2 = "b"
s3 = "b"
print(isInterleave(s1, s2, s3))
# Output: true

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(isInterleave(s1, s2, s3))
# Output: true

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
print(isInterleave(s1, s2, s3))
# Output: false

s1 = ""
s2 = ""
s3 = ""
print(isInterleave(s1, s2, s3))
# Output: true