# Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
h = 5
w = 4
horizontalCuts = [3,1]
verticalCuts = [1]

horizontalCuts = [0] + horizontalCuts + [h]
verticalCuts = [0] + verticalCuts + [w]

horizontalCuts.sort()
verticalCuts.sort()

maxh = 0
for i in range(1,len(horizontalCuts)):
    if horizontalCuts[i] - horizontalCuts[i-1] > maxh:
        maxh = horizontalCuts[i] - horizontalCuts[i-1]
    
maxw = 0
for i in range(1,len(verticalCuts)):
    if verticalCuts[i] - verticalCuts[i-1] > maxw:
        maxw = verticalCuts[i] - verticalCuts[i-1]

print((maxh*maxw)%(10**9+7))