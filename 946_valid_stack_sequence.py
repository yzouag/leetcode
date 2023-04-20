from typing import List

def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
    stack = []

    i = 0
    j = 0

    n = len(pushed)

    while j < n:
        if not stack:
            stack.append(pushed[i])
            i += 1
            continue

        if stack[-1] == popped[j]:
            stack.pop()
            j += 1
        else:
            if i == n:
                return False
            stack.append(pushed[i])
            i += 1

    return len(stack) == 0

pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
print(validateStackSequences(pushed, popped))
# Output: true

pushed = [1,2,3,4,5]
popped = [4,3,5,1,2]
print(validateStackSequences(pushed, popped))
# Output: false