# Array Of Products

array = [5, 1, 4, 2]  # [8,40,10,20]

# Naive Solution
"""
    simply go through the array and initialize runningProducts = 1 
    create a record of running product when the index are not same,
    and return it.
"""
# Time Complexity = O(n^2) || Space Complexity = O(n)


def arrayOfProducts(array):
    products = []
    for i in range(len(array)):
        runningProducts = 1
        for j in range(len(array)):
            if i != j:
                runningProducts *= array[j]
        products.append(runningProducts)

    return products


# Optimized Solution
"""
    Creating an array product going through the array and inserting leftproduct(prefix) and then 
    in reverse order inserting the right running product(suffix) in the same array 
"""
# Time Complexity = O(n) || Space Complexity = O(n)
def arrayOfProducts1(array):
    products = [1 for _ in range(len(array))]

    leftRunningProduct = 1
    for i in range(len(array)):
        products[i] = leftRunningProduct
        leftRunningProduct *= array[i]

    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        products[i] *= rightRunningProduct
        rightRunningProduct *= array[i]

    return products


print(arrayOfProducts(array))
print(arrayOfProducts1(array))
