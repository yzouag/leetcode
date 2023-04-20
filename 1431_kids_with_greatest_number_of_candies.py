from typing import List

def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    max_candies = max(candies)
    return list(map(lambda x: x+extraCandies >= max_candies, candies))

candies = [2,3,5,1,3]
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))
# Output: [true,true,true,false,true]

candies = [4,2,1,1,2]
extraCandies = 1
print(kidsWithCandies(candies, extraCandies))
# Output: [true,false,false,false,false]
