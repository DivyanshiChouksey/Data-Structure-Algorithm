array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]


def productSum(array, multiplier=1):
    sum = 0
    for ele in array:
        if type(ele) is list:
            sum += productSum(ele, multiplier + 1)
        else:
            sum += ele
    return sum * multiplier


print(productSum(array))
