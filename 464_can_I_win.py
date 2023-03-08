from typing import Tuple
def canIWin(maxChoosableInteger: int, desiredTotal: int) -> bool:
    if (maxChoosableInteger+1) * maxChoosableInteger // 2 < desiredTotal:
        return False
    
    integers = tuple(range(1, maxChoosableInteger+1))
    seen = {}
    
    def dfs(integers: Tuple[int], remain) -> bool:
        if integers[-1] >= remain:
            return True
        
        if integers in seen:
            return seen[integers]
        
        for i in range(len(integers)): # pick any number, see if we can make the next player lose
            afterPick = integers[:i] + integers[i+1:]
            if dfs(afterPick, remain-integers[i]) == False:
                seen[integers] = True
                return True
        
        seen[integers] = False
        return False
    
    return dfs(integers, desiredTotal)


maxChoosableInteger = 10
desiredTotal = 11
print(canIWin(maxChoosableInteger, desiredTotal))
# Output: false

maxChoosableInteger = 10
desiredTotal = 0
print(canIWin(maxChoosableInteger, desiredTotal))
# Output: true

maxChoosableInteger = 10
desiredTotal = 1
print(canIWin(maxChoosableInteger, desiredTotal))
# Output: true