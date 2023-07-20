from typing import List
def nextGreatestLetter(letters: List[str], target: str) -> str:
    res = None
    for l in letters:
        if l > target:
            if res and l < res:
                res = l
            elif not res:
                res = l
    return res if res else letters[0]

letters = ["c","f","j"]
target = "a"
print(nextGreatestLetter(letters, target))
# Output: "c"

letters = ["c","f","j"]
target = "c"
print(nextGreatestLetter(letters, target))
# Output: "f"

letters = ["x","x","y","y"]
target = "z"
print(nextGreatestLetter(letters, target))
# Output: "x"