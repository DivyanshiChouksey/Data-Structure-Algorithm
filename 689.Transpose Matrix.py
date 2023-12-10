# Transpose Matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]


def transpose(matrix):
    return zip(*matrix)


print(transpose(matrix))
