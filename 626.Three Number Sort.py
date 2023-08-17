# Three Number Sort

# Naive solution
array = [1, 0, 0, -1, -1, 0, 1, 1]
order = [0, 1, -1]

def threeNumberSort(array, order):
    zero = one = nvg = 0
    for n in array:
        if n==order[0]:
            zero+=1
        elif n==order[1]:
            one +=1
        else:
            nvg +=1

    ans = []
    while zero>0:
        ans.append(order[0])
        zero-=1
    while one>0:
        ans.append(order[1])
        one-=1
    while nvg>0:
        ans.append(order[2])
        nvg-=1
        
    return ans

print(threeNumberSort(array, order))




array = [7, 8, 9, 7, 8, 9, 9, 9, 9, 9, 9, 9]
order = [8, 7, 9]

def threeNumberSort(array, order):
    firstIdx = 0
    for i in range(len(array)):
        if array[i]==order[0]:
            array[i],array[firstIdx] = array[firstIdx],array[i]
            firstIdx+=1

    lastIdx = len(array)-1
    for i in range(len(array)-1,-1,-1):
        if array[i] == order[2]:
            array[i],array[lastIdx] = array[lastIdx],array[i]
            lastIdx-=1
            
    return array

print(threeNumberSort(array, order))



array = [7, 8, 9, 7, 8, 9, 9, 9, 9, 9, 9, 9]
order = [8, 7, 9]

def threeNumberSort(array, order):
    first = 0
    second = 0
    third = len(array)-1

    while second <=third:
        if array[second] == order[0]:
            array[second],array[first] = array[first] , array[second]
            first += 1
            second+=1
        elif array[second] == order[1]:
            second+=1
        else:
            array[second] , array[third] = array[third],array[second]
            third-=1

    return array


print(threeNumberSort(array, order))
