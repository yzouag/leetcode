from typing import List

# main idea: BFS
# BFS cannot go back to visited states
# make same grid different states as we have keys
# using a bit masking to represent this state
# at start, 00000, then after getting some keys 010010
def shortestPathAllKeys(grid: List[str]) -> int:
    num_keys = 0
    lock_set = set()
    key_set = set()
    start = (0, 0)
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '@':
                start = (i, j)
            elif grid[i][j] in 'abcdef': # in requirement there are at most 6 keys
                num_keys += 1
                key_set.add(grid[i][j])
            elif grid[i][j] in 'ABCDEF':
                lock_set.add(grid[i][j])

    queue = [(start, 0)] # [(pos, state)] initial state is 0000
    directions = [(0,1), (0,-1), (-1,0), (1,0)]
    steps = -1
    visited = set()
    while queue:
        temp = []
        for node, state in queue:
            if state == 2**num_keys-1:
                return steps
            if node[0] < 0 or node[0] >= m or node[1] < 0 or node[1] >= n: # invalid cell
                continue
            if (node, state) in visited: # visited cell
                continue
            
            visited.add((node, state))
            cell = grid[node[0]][node[1]]
            
            if cell == '#': # wall
                continue
            elif cell in lock_set: # lock
                if (1 << (ord(cell) - ord('A'))) & state == 0:
                    continue
            elif cell in key_set: # key
                if (1 << (ord(cell) - ord('a'))) & state == 0:
                    state += 1 << (ord(cell) - ord('a'))
            
            for dir in directions:
                new_x = node[0] + dir[0]
                new_y = node[1] + dir[1]
                temp.append(((new_x, new_y), state))
        queue = temp
        steps += 1
    return -1
        

grid = ["@.a..","###.#","b.A.B"]
print(shortestPathAllKeys(grid))
# Output: 8

grid = ["@..aA","..B#.","....b"]
print(shortestPathAllKeys(grid))
# Output: 6

grid = ["@Aa"]
print(shortestPathAllKeys(grid))
# Output: -1

grid = ["@...a",".###A", "b.BCc"]
print(shortestPathAllKeys(grid))
# Output: 10

grid = ["Dd#b@", ".fE.e", "##.B.", "#.cA.","aF.#C"]
print(shortestPathAllKeys(grid))
# Output: 14
