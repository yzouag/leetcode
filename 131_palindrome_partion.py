from typing import List
def partition(s: str) -> List[List[str]]:
    res = []
    def isPalindrome(s: str) -> bool:
        l, r = 0, len(s)-1
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def dfs(remains: str, intermediate_res: List[str]):
        if len(remains) == 0:
            res.append(intermediate_res)
            return
        
        for i in range(1, len(remains)+1):
            substr = remains[:i]
            if isPalindrome(substr):
                new_intermediate_res = intermediate_res + [substr]
                dfs(remains[i:], new_intermediate_res)
    
    dfs(s, [])
    return res


s = "aab"
print(partition(s))
# Output: [["a","a","b"],["aa","b"]]

s = "a"
print(partition(s))
# Output: [["a"]]