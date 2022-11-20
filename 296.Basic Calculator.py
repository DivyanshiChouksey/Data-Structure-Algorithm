# Basic Calculator

"""
    Simple iterative solution by identifying characters one by one
    One important thing is that the input is valid, which means the parentheses are always paired and in order.
    Only 5 possible input we need to pay attention:

    1. digit: it should be one digit from the current number
    2. '+': number is over, we can add the previous number and start a new number
    3. '-': same as above
    4. '(': push the previous result and the sign into the stack, set result to 0, just calculate the new result within the parenthesis.
    5. ')': pop out the top two numbers from stack, first one is the sign before this pair of parenthesis, second is the temporary result before this pair of parenthesis. We add them together.
    
    Finally if there is only one number, from the above solution, we haven't add the number to the result, so we do a check see if the number is zero.
"""


# Time Complexity = O(n) || Space Complexity = O(n)

s = "(1+(4+5+2)-3)+(6+8)"


def calculate(s):
    if s == "":
        return 0

    result = 0
    sign = 1
    num = 0

    stack = [sign]
    """
    97 + 23
    """
    for ch in s:
        if "0" <= ch and ch <= "9":
            num = num * 10 + int(ch)
        elif ch == "+" or ch == "-":
            result += sign * num
            sign = stack[-1] * (1 if ch == "+" else -1)
            num = 0
        elif ch == "(":
            stack.append(sign)

        elif ch == ")":
            stack.pop()

    result += sign * num
    return result


print(calculate(s))
