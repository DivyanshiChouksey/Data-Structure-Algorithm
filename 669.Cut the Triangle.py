# Cut the Triangle

"""
Input - test case consists of four lines. The first of them is empty.

4
# an empty space 
1 1
1 2
2 1
# an empty space 
1 1
1 2
2 2
# an empty space 
4 7
6 8
3 5
# an empty space 
4 5
4 7
6 8

"""

"""
Output
NO
NO
YES
YES

"""

for _ in range(int(input())):
    tmp = input()
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    x3,y3 = map(int,input().split())

    if (x1==x2 or x2==x3 or x1==x3) and (y1==y2 or y1==y3 or y2==y3):
        print("No")
    else:
        print("Yes")
