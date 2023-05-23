import functools
def removeKdigits(num: str, k: int) -> str:
    stack = []
    for ch in num:
        while stack and k > 0 and stack[-1] > ch:
            stack.pop()
            k -= 1
        
        if stack or ch != '0':
            stack.append(ch)
    
    if k > 0:
        stack = stack[:-k]
    return ''.join(stack) or '0'

num = "1432219"
k = 3
print(removeKdigits(num, k))
# Output: "1219"

num = "10200"
k = 1
print(removeKdigits(num, k))
# Output: "200"

num = "10"
k = 2
print(removeKdigits(num, k))
# Output: "0"