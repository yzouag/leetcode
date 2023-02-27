from collections import defaultdict
from typing import List

def totalFruit(fruits: List[int]) -> int:
    # l, r = 0, 0
    # res = 0
    # window = defaultdict(int)
    # while r < len(fruits):
    #     if len(window) <= 2:
    #         window[fruits[r]] += 1
    #         r += 1
    #     else:
    #         res = max(res, r-l-1)
    #         window[fruits[l]] -= 1
    #         if window[fruits[l]] == 0:
    #             window.pop(fruits[l])
    #         l += 1
    # if len(window) <= 2:
    #     res = max(res, r-l)
    # else:
    #     res = max(res, r-l-1)
    # return res

    # solution:
    # Hash map 'basket' to store the types of fruits.
    basket = {}
    left = 0
    
    # Add fruit from the right index (right) of the window.
    for right, fruit in enumerate(fruits):
        basket[fruit] = basket.get(fruit, 0) + 1

        # If the current window has more than 2 types of fruit,
        # we remove one fruit from the left index (left) of the window.
        if len(basket) > 2:
            basket[fruits[left]] -= 1

            # If the number of fruits[left] is 0, remove it from the basket.
            if basket[fruits[left]] == 0:
                del basket[fruits[left]]
            left += 1
    
    # Once we finish the iteration, the indexes left and right 
    # stands for the longest valid subarray we encountered.
    return right - left + 1

fruits = [1,2,1]
print(totalFruit(fruits))
# Output: 3

fruits = [0,1,2,2]
print(totalFruit(fruits))
# Output: 3

fruits = [1,2,3,2,2]
print(totalFruit(fruits))
# Output: 4

fruits = [3,3,3,1,2,1,1,2,3,3,4]
print(totalFruit(fruits))
# Output: 5

fruits = [0,1,2]
print(totalFruit(fruits))
# Output: 2