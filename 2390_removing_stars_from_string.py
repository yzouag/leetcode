def removeStars(s: str) -> str:
    num_stars = 0
    res = []

    for ch in s:
        if ch == '*':
            if not res:
                num_stars += 1
            else:
                res.pop()
        else:
            if num_stars > 0:
                continue
            res.append(ch)
    return "".join(res)

s = "leet**cod*e"
print(removeStars(s))
# Output: "lecoe"


s = "erase*****"
print(removeStars(s))
# Output: ""