def judgeCircle(moves: str) -> bool:
    start = [0, 0]
    move = {"U":(0,1), "D":(0,-1), "L":(-1,0), "R": (1, 0)}
    for mov in moves:
        start[0] += move[mov][0]
        start[1] += move[mov][1]
    return start == [0,0] 

moves = "UD"
print(judgeCircle(moves))
# Output: true

moves = "LL"
print(judgeCircle(moves))
# Output: false