from typing import List

def getRow(rowIndex: int) -> List[int]:
    if rowIndex == 0:
        return [1]
    ans = getRow(rowIndex-1)
    res = [1]
    for i in range(len(ans)-1):
        res.append(ans[i]+ans[i+1])
    res.append(1)
    return res

rowIndex = 3
print(getRow(rowIndex))
# Output: [1,3,3,1]

rowIndex = 0
print(getRow(rowIndex))
# Output: [1]

rowIndex = 1
print(getRow(rowIndex))
# Output: [1, 1]