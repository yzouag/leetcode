from collections import Counter

def isScramble(s1: str, s2: str) -> bool:
    memo = {}

    def recursion(i1, j1, i2, j2) -> bool:
        if (i1, j1, i2, j2) in memo:
            return memo[(i1, j1, i2, j2)]
        
        sub_s1 = s1[i1:j1]
        sub_s2 = s2[i2:j2]

        # base case
        if len(sub_s1) == 1:
            return sub_s1 == sub_s2
        
        if Counter(sub_s1) != Counter(sub_s2):
            memo[(i1, j1, i2, j2)] = False
            return False
        
        
        for i in range(1, len(sub_s1)):
            s2_head = s2[i2:i2+i]
            s2_tail = s2[i2+i:j2]

            # 1. no reverse
            s1_head = s1[i1:i1+i]
            s1_tail = s1[i1+i:j1]

            if Counter(s2_head) == Counter(s1_head) and Counter(s2_tail) == Counter(s1_tail):
                if recursion(i1, i1+i, i2, i2+i) and recursion(i1+i, j1, i2+i, j2):
                    memo[(i1, j1, i2, j2)] = True
                    return True

            # 2. reverse
            s1_head = s1[j1-i:j1]
            s1_tail = s1[i1:j1-i]

            if Counter(s2_head) == Counter(s1_head) and Counter(s2_tail) == Counter(s1_tail):
                if recursion(j1-i, j1, i2, i2+i) and recursion(i1, j1-i, i2+i, j2):
                    memo[(i1, j1, i2, j2)] = True
                    return True
        
        memo[(i1, j1, i2, j2)] = False
        return False

    return recursion(0, len(s1), 0, len(s1))

s1 = "great"
s2 = "rgeat"
print(isScramble(s1, s2))
# Output: true

s1 = "abcde"
s2 = "caebd"
print(isScramble(s1, s2))
# Output: false

s1 = "a"
s2 = "a"
print(isScramble(s1, s2))
# Output: true