# Minimum Penalty for a Shop

# Time : O(n)
# Space : O(1)

customers = "YYYNYYN"

def bestClosingTime(customers):
    maxHour = 0
    idx = 0
    tmp = 0
    for i in range(len(customers)):
        if customers[i] == "Y":
            tmp+=1
        else:
            tmp-=1
        if tmp>maxHour:
            maxHour = tmp
            idx = i+1

    return idx


print( bestClosingTime(customers))
