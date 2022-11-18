def removeDuplicates(s: str) -> str:
    queue = []
    for char in s:
        if queue and queue[-1] == char:
            queue.pop()
        else:
            queue.append(char)
    return "".join(queue)

s = "abbaca"
print(removeDuplicates(s))
# Output: "ca"

s = "azxxzy"
print(removeDuplicates(s))
# Output: "ay"