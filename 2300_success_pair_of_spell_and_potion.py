from typing import List
# from bisect import bisect_left
# from math import ceil

def successfulPairs(spells: List[int], potions: List[int], success: int) -> List[int]:
    potions.sort()
    spells = list(zip(spells, list(range(len(spells)))))
    spells.sort()

    at_least_index = len(potions)-1

    res = [0] * len(spells)
    for spell, index in spells:
        while at_least_index >= 0 and potions[at_least_index] * spell >= success:
            at_least_index -= 1
        res[index] = len(potions)-at_least_index-1

    return res

spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7
print(successfulPairs(spells, potions, success))
# Output: [4,0,3]

spells = [3,1,2]
potions = [8,5,8]
success = 16
print(successfulPairs(spells, potions, success))
# Output: [2,0,2]

spells = [1,2,3,4,5,6,7]
potions = [1,2,3,4,5,6,7]
success = 25
print(successfulPairs(spells, potions, success))
