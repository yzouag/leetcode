import itertools


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # my solution, too long
        """
        ptr1, ptr2 = len(s)-1, len(t)-1

        while ptr1 >= 0 or ptr2 >= 0:
            skip = 0
            while ptr1 >= 0 and (s[ptr1] == '#' or skip > 0):
                if s[ptr1] == '#':
                    skip += 1
                    ptr1 -= 1
                else:
                    skip -= 1
                    ptr1 -= 1

            skip = 0
            while ptr2 >= 0 and (t[ptr2] == '#' or skip > 0):
                if t[ptr2] == '#':
                    skip += 1
                    ptr2 -= 1
                else:
                    skip -= 1
                    ptr2 -= 1
            
            if ptr1 < 0 and ptr2 >= 0 and t[ptr2] != '':
                return False
            if ptr1 >= 0 and ptr2 < 0 and s[ptr1] != '':
                return False

            if s[ptr1] != t[ptr2]:
                return False
            ptr1 -= 1
            ptr2 -= 1
        
        return True
        """
        
        # method 1: make a new string:
        """
        def build(s: str) -> str:
            res = []
            for i in range(len(s)):
                if s[i] == '#' and res:
                    res.pop()
                else:
                    res.append(s[i])
            return "".join(res)
        return build(s) == build(t)
        """

        # method 2: two pointers
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.zip_longest(F(s), F(t)))


if __name__ == "__main__":
    s = "ab#c"
    t = "ad#c"
    assert Solution().backspaceCompare(s, t) == True

    s = "ab##"
    t = "c#d#"
    assert Solution().backspaceCompare(s, t) == True

    s = "a#c"
    t = "b"
    assert Solution().backspaceCompare(s, t) == False

    s = "a###c"
    t = "c"
    assert Solution().backspaceCompare(s, t) == True