def countSubstrings(s: str) -> int:
    N = len(s)
    result = 0
    
    for i in range(2*N-1):
        left = i//2
        right = (i+1)//2
        while left >= 0 and right < N and s[left] == s[right]:
            result += 1
            left -= 1
            right += 1
    
    return result

s = "abc"
print(countSubstrings(s)) # 3

s = "aaa"
print(countSubstrings(s)) # 6