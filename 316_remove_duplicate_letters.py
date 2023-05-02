def removeDuplicateLetters(s: str) -> str:
    last_occ = {}
    stack = []

    # last_occ store the last occurrence of the letter in s
    for i in range(len(s)):
        last_occ[s[i]] = i

    # s[i] in stack, skip
    # not in stack, first pop all the letters that are lexical larger and will appear later
    # then append s[i] to the stack
    for i in range(len(s)):
        if s[i] not in stack:
            while (stack and stack[-1] > s[i] and last_occ[stack[-1]] > i):
                stack.pop()
            stack.append(s[i])

    return ''.join(stack)


    

s = "bcabc"
print(removeDuplicateLetters(s))
# Output: "abc"

s = "cbacdcbc"
print(removeDuplicateLetters(s))
# Output: "acdb"