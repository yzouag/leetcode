from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # method 1:
        # comp_list = [['']]
        # for i in range(1,n+1):
        #     res = []
            
        #     for j in range(i):
        #         for left in comp_list[i-1-j]:
        #             for right in comp_list[j]:
        #                 res.append( '(' + left + ')' + right)
                        
        #     comp_list.append(res)
        # return comp_list[-1]

        ans = []
        def backtrack(S = [], left = 0, right = 0):
            # if reach the length, exit
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans

if __name__ == "__main__":
    n = 3
    # ["((()))","(()())","(())()","()(())","()()()"]
    print(Solution().generateParenthesis(n))
    
    n = 2
    # ["()()", "(())"]
    print(Solution().generateParenthesis(n))
    
    n = 1
    # ["()"]
    print(Solution().generateParenthesis(n))
    