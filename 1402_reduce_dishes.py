from typing import List

def maxSatisfaction(satisfaction: List[int]) -> int:
    satisfaction.sort()
    if satisfaction[-1] < 0:
        return 0
    
    res = 0
    non_neg = 0
    neg = 0

    i = 0
    while satisfaction[i] < 0:
        i += 1
    for j in range(i, len(satisfaction)):
        non_neg += satisfaction[j]
        res += satisfaction[j] * (j-i+1)
    while i > 0:
        i -= 1
        neg += satisfaction[i]
        if non_neg + neg > 0:
            res += non_neg + neg
        else:
            break
    return res

satisfaction = [-1,-8,0,5,-9]
print(maxSatisfaction(satisfaction))
# Output: 14

satisfaction = [4,3,2]
print(maxSatisfaction(satisfaction))
# Output: 20

satisfaction = [-1,-4,-5]
print(maxSatisfaction(satisfaction))
# Output: 0