class Solution:
    def isValid(self, s: str) -> bool:
        # why stack? 
        # ({)} is invalid, the parenthese must be popped in correct order
        # the current stack is ({, we expect next to be } but not )
        # so we pop the last element of stack, {, and find its corresponding value }
        # if next is not } it should be error
        paren_dict = {"(":")", "{":"}", "[":"]"}
        stack = []
        for character in s:
            if character in paren_dict:
                stack.append(character) # add one left parenthese to the stack
            elif len(stack) == 0 or paren_dict[stack.pop()] != character:
                return False
        return len(stack) == 0

if __name__ == "__main__":
    s = "()"
    assert True == Solution().isValid(s)
    
    s = "()[]{}"
    assert True == Solution().isValid(s)

    s = "(]"
    assert False == Solution().isValid(s)

    s = "({)}"
    assert False == Solution().isValid(s)