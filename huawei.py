# 现有一个字符串，组成字符串的字符包括 ( ) { } [ ]六种括号和其它字符。
# 出现以下一种情况视为无效字符串：
# 1、任一类型的左右括号数量不相等；
# 2、存在未按正确顺序（先左后右）闭合的括号；
# {(})
# 输出括号的最大嵌套深度，若字符串无效则输出0
# 举例：
# 输入
# ({4}.[{2}]1)
# 1234
# 输出
# 3
# 
# ((( ))


def solution(input: str):
    stack = []
    max_depth = 0
    depth = 0

    for i in range(len(input)):
        if input[i] == '(' or input[i] == '{' or input[i] == '[':
            stack.append(input[i])
            depth += 1
            max_depth = max(depth, max_depth)
        elif input[i] == ')' or input[i] == '}' or input[i] == ']':
            if len(stack) == 0:
                return 0
            if input[i] == ')' and stack[-1] != '(':
                return 0
            elif input[i] == '}' and stack[-1] != '{':
                return 0
            elif input[i] == ']' and stack[-1] != '[':
                return 0
            else:
                stack.pop()
                depth -= 1

    if len(stack) != 0:
        return 0
    return max_depth

# input = '({4}.[{2}]1)' # 3
# print(solution(input))

# input = '({4)'
# print(solution(input)) # 0

# input = '((())'
# print(solution(input)) # 0


# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
# 此外，你可以假设该网格的四条边均被水包围。


# 示例 1：
# 输入：grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# 输出：1

# 示例 2：
# 输入：grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# 输出：3
 

# 提示：
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] 的值为 '0' 或 '1'

from typing import List
def numIslands(grid: List[List[str]]):
    m = len(grid)
    n = len(grid[0])

    result = 0
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    for i in range(m):
        for j in range(n):
            if (grid[i][j] == '1'):
                result += 1
                stack = [(i, j)]
                while stack:
                    temp = []
                    for node in stack:
                        x, y = node
                        grid[x][y] = '*'
                        for dir in directions:
                            new_x = x + dir[0]
                            new_y = y + dir[1]
                            if (new_x >= 0 and new_x < m and new_y >= 0 and new_y < n):
                                if (grid[new_x][new_y] == '1'):
                                    temp.append((new_x, new_y))
                    stack = temp

    return result

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(numIslands(grid)) # 1

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(numIslands(grid)) # 3