# Maximum Units on a Truck
boxTypes =[[5,10],[2,5],[4,7],[3,9]]
truckSize = 10
ans = 0
boxTypes.sort(key = lambda x : x[1], reverse = True)
for boxType in boxTypes:
    if truckSize >=0:    
        if boxType[0] <= truckSize:
            ans += boxType[0] * boxType[1]
            truckSize -= boxType[0]
        else:
            ans += truckSize * boxType[1] 
            truckSize -= boxType[0]
print(ans)
