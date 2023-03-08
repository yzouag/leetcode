def canReach(s: str, minJump: int, maxJump: int) -> bool:
    n = len(s)
    if s[n-1] == '1':
        return False
    
    memo = {}
    def dfs(i):
        if n-1-i >= minJump and n-1-i <= maxJump:
            memo[i] = True
            return True
        

s = "011010"
minJump = 2
maxJump = 3
print(canReach(s, minJump, maxJump))
# Output: true

s = "01101110"
minJump = 2
maxJump = 3
print(canReach(s, minJump, maxJump))
# Output: false