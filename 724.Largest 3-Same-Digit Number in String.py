# Largest 3-Same-Digit Number in String

num = "6777133339"


def largestGoodInteger(num):
    # Assign 'max_digit' to NUL character (smallest ASCII value character)
    max_digit = '\0'

    # Iterate on characters of the num string.
    for index in range(len(num) - 2):
        # If 3 consecutive characters are the same,
        # store the character in 'max_digit' if it's bigger than what it already stores.
        if num[index] == num[index + 1] == num[index + 2]:
            max_digit = max(max_digit, num[index])

    # If 'max_digit' is NUL, return an empty string; otherwise, return a string of size 3 with 'max_digit' characters.
    return '' if max_digit == '\0' else max_digit * 3



print(largestGoodInteger(num))
