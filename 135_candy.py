from typing import List

# key discovery:
# the number of continuous slope means how many extra candies we need to allocate
# 1 2 3 4 2 1 => down slope 2, up slope 4
# 1 2 3 4 4 5 6 => two up slope, with each length 4, 3


def candy(ratings: List[int]) -> int:
    up = 1
    down = 0
    res = 1
    peak = 0

    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i - 1]:
            up += 1
            down = 0
            res += up
            peak = up

        elif ratings[i] == ratings[i - 1]:
            down = 0
            peak = 0
            up = 1
            res += 1

        else:
            down += 1
            up = 1
            res += down
            if peak <= down:
                res += 1

    return res


ratings = [1, 0, 2]
print(candy(ratings))
# Output: 5

ratings = [1, 2, 2]
print(candy(ratings))
# Output: 4

ratings = [1, 2, 3]
print(candy(ratings))
# Output: 6

ratings = [1, 2, 3, 4, 4, 5, 6]
print(candy(ratings))
# Output: 16

ratings = [1, 3, 2, 2, 1]
print(candy(ratings))
# Output: 7
