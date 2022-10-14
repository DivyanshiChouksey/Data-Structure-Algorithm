# Ball coloring

# Time Complexity = O(n^2) || Space Complexity = O(1)

n = 1


def ballColoring1(n):
    return n**2 - n + 2


def ballColoring(n):
    if n == 1:
        return 2
    num1 = fact(n - 2)
    num2 = fact(n)
    return (num2 // num1) + 2


def fact(m):
    f = 1
    for i in range(1, m + 1):
        f *= i
    return f


print(ballColoring(n))
print(ballColoring1(n))
