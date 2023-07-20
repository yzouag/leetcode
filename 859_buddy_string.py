from collections import Counter
def buddyStrings(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False
    
    diff = []
    for i in range(len(s)):
        if s[i] != goal[i]:
            diff.append((s[i], goal[i]))
    
    if len(diff) == 0:
        if Counter(s).most_common(1)[0][1] > 1:
            return True

    if len(diff) != 2:
        return False
    
    return diff[0][0] == diff[1][1] and diff[0][1] == diff[1][0]
    

s = "ab"
goal = "ba"
print(buddyStrings(s, goal))
# Output: true

s = "ab"
goal = "ab"
print(buddyStrings(s, goal))
# Output: false

s = "aa"
goal = "aa"
print(buddyStrings(s, goal))
# Output: true