from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        union_set = {a: a for a in range(0,26)} # initialize, a must equal to a
        def find(x):
            if x == union_set[x]:
                return x
            return find(union_set[x]) # get the root representation

        def connect(x, y):
            a = find(x)
            b = find(y)
            union_set[b] = a
        
        for a, e, _, b in equations:
            if e == '=': # first join all the equal symbol
                connect(ord(a)-ord('a'), ord(b)-ord('a'))
        for a, e, _, b in equations:
            if e == '!':
                if find(ord(a)-ord('a')) == find(ord(b)-ord('a')):
                    return False
        return True


if __name__ == "__main__":
    equations = ["a==b","b!=a"]
    assert Solution().equationsPossible(equations) == False

    equations = ["b==a","a==b"]
    assert Solution().equationsPossible(equations) == True