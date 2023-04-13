#  Validate Stack Sequences

"""
  For each value, push it to the stack.
  Then, greedily pop values from the stack if they are the next values to pop.
  At the end, we check if we have popped all the values successfully.
"""


pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]


def validateStackSequences(pushed, popped):
    j = 0
    stack = []
    for push in pushed:
        stack.append(push)
        while stack!=[] and  stack[-1]==popped[j]:
            stack.pop()
            j+=1
    return j==len(popped)
