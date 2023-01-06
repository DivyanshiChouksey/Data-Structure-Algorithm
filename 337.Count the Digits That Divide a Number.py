# Count the Digits That Divide a Number

# Time Complexity = O(n) || Space Complexity = O(1)
num = 1248


def countDigits(num):
    count = 0
    for n in str(num):
        if num % int(n) == 0:
            count += 1
    return count


print(countDigits(num))
