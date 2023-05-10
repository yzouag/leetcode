def isRobotBounded(instructions: str) -> bool:
    init = [0, 0]
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    current_dir = 0
    for ins in instructions:
        if ins == 'L':
            current_dir -= 1
            if current_dir < 0:
                current_dir += 4
        elif ins == 'R':
            current_dir += 1
            if current_dir > 3:
                current_dir -= 4
        else:
            init[0] += directions[current_dir][0]
            init[1] += directions[current_dir][1]
    if init[0] == 0 and init[1] == 0:
        return True
    if current_dir != 0:
        return True
    return False

instructions = "GGLLGG"
print(isRobotBounded(instructions))
# Output: true

instructions = "GG"
print(isRobotBounded(instructions))
# Output: false

instructions = "GL"
print(isRobotBounded(instructions))
# Output: true