def decodeString(s: str) -> str:
    stack = []
    res = ""

    num = 0
    for ch in s:
        if ch.isdigit():
            num = num*10 + int(ch)
        elif ch == "[":
            stack.append([num, ""])
            num = 0
        elif ch == "]":
            inner_num, inner_pattern = stack.pop()
            if not stack:
                res += inner_num * inner_pattern
            else:
                stack[-1][1] += inner_num * inner_pattern
        else:
            if not stack:
                res += ch
            else:
                stack[-1][1] += ch
    return res
        

        

s = "3[a]2[bc]"
print(decodeString(s))
# Output: "aaabcbc"

s = "3[a2[c]]"
print(decodeString(s))
# Output: "accaccacc"

s = "2[abc]3[cd]ef"
print(decodeString(s))
# Output: "abcabccdcdcdef"