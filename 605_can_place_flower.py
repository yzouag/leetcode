from typing import List

def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    if n == 0:
        return True
    
    if len(flowerbed)-sum(flowerbed) < n:
        return False
    
    flowers = 0
    flowerbed.append(0)
    flowerbed.insert(0, 0)
    num_empty = 0
    for pos in flowerbed:
        if pos == 1:
            if num_empty > 0: flowers += (num_empty-1) // 2
            num_empty = 0
        else:
            num_empty += 1
        if flowers >= n:
            return True
    if num_empty > 0: flowers += (num_empty-1) // 2
    return flowers >= n

flowerbed = [1,0,0,0,1]
n = 1
print(canPlaceFlowers(flowerbed, n))
# Output: true

flowerbed = [1,0,0,0,1]
n = 2
print(canPlaceFlowers(flowerbed, n))
# Output: false

flowerbed = [1,0,0,0,1,0,0]
n = 2
print(canPlaceFlowers(flowerbed, n))
# Output: true