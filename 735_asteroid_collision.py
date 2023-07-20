from typing import List

def asteroidCollision(asteroids: List[int]) -> List[int]:
    stack = []
    for asteroid in asteroids:
        if not stack:
            stack.append(asteroid)
        elif asteroid > 0:
            stack.append(asteroid)
        else:
            live = False
            while stack:
                if stack[-1] < 0:
                    live = False
                    stack.append(asteroid)
                    break
                if stack[-1] < -asteroid:
                    stack.pop()
                    live = True
                elif stack[-1] == -asteroid:
                    live = False
                    stack.pop()
                    break
                else:
                    live = False
                    break
            if live:
                stack.append(asteroid)
    return stack

asteroids = [5,10,-5]
print(asteroidCollision(asteroids))
# Output: [5,10]

asteroids = [8,-8]
print(asteroidCollision(asteroids))
# Output: []

asteroids = [10,2,-5]
print(asteroidCollision(asteroids))
# Output: [10]