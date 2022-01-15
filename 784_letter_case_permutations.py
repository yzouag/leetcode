from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        stack = [(s, '')]
        result = []
        while stack:
            remains, used = stack.pop()
            if len(remains) == 0:
                result.append(used)
            else:
                if remains[0].isalpha():
                    new_remains = remains[1:]
                    # if remains[0].isupper():
                    #     new_used = used + remains[0].lower()
                    # else:
                    #     new_used = used + remains[0].upper()
                    new_used = used + remains[0].swapcase()
                    stack.append((new_remains, new_used))
                used += remains[0]
                remains = remains[1:]
                stack.append((remains, used))
        return result

if __name__ == "__main__":
    s = "a1b2"
    print(Solution().letterCasePermutation(s))