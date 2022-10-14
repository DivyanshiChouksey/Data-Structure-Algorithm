# Valid Starting City

distances = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3]
mpg = 10


def validStartingCity(distances, fuel, mpg):
    cities = len(distances)

    for i in range(cities):
        milesLeft = 0
        for j in range(i, i + cities):
            if milesLeft < 0:
                continue
            j = j % cities
            milesLeft += (fuel[j] * mpg) - distances[j]

        if milesLeft >= 0:
            return i


def validStartingCity2(distances, fuel, mpg):
    cities = len(distances)
    milesLeft = 0

    idx = 0
    miles = 0

    for i in range(1, cities):
        milesLeft += fuel[i - 1] * mpg - distances[i - 1]

        if milesLeft < miles:
            miles = milesLeft
            idx = i
    return idx


print(validStartingCity(distances, fuel, mpg))
print(validStartingCity2(distances, fuel, mpg))
