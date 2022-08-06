# Asteroids Collision
"""
    Starting with a stack initialise it with the first element of asteroid
    check until the previous value in stack is a positive value and current value is negative then
    if absolute of negative value is greater then pop one value from stack or 
    absolute value of both element is equal then also pop the value from stack
    otherwise append element of asteroid in our stack and return stack.

"""
# Time Complexity = O(n) , n=2n
# Space Complexity = O(n)

asteroids = [5, 10, -15]


def asteroidCollision(asteroids):
    stack = [asteroids[0]]
    for asteroid in asteroids:
        while stack and asteroid < 0 < stack[-1]:
            if stack[-1] < abs(asteroid):
                stack.pop()
                continue
            elif stack[-1] == abs(asteroid):
                stack.pop()
            break
        else:
            stack.append(asteroid)
    return stack


print(asteroidCollision(asteroids))
