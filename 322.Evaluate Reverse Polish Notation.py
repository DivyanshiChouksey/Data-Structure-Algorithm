# Evaluate Reverse Polish Notation

"""
    Using stack data structure loop through the given array,
    1.Push the value into the stack until any of these "+" "-","*","/" operators are found after that pop two values 
        from the stack and
    2.Then check which operator matches to the current element and perform the operation of that operator on the 
        previous two values and push this new values into the stack 
    3.Again repeated step 1 and step2 and at the end return the top element of stack 

    NOTE - for divide operator Divide and convert it to integer value (eg- int(b / a))
"""

# Time Complexity = O(n) || Space Complexity = O(n)

tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]


def evalRPN(tokens):
    stack = []
    for n in tokens:
        if n not in ("+", "*", "-", "/"):
            stack.append(n)
        else:
            a = int(stack.pop())
            b = int(stack.pop())
            if n == "+":
                stack.append(a + b)

            elif n == "-":
                stack.append(b - a)

            elif n == "*":
                stack.append(a * b)

            else:
                stack.append(int(b / a))

    return int(stack[-1])


print(evalRPN(tokens))
