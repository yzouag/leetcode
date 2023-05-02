import math
def bulbSwitch(n: int) -> int:
    return math.floor(math.sqrt(n))    

n = 3
print(bulbSwitch(n))
# Output: 1

n = 0
print(bulbSwitch(n))
# Output: 0

n = 1
print(bulbSwitch(n))
# Output: 1