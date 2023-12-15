# Destination City

paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]

def destCity(paths):
    seen = set()
    for i in range(len(paths)):
        seen.add(paths[i][0])

    for i in range(len(paths)):
        if paths[i][1] not in seen:
            return paths[i][1]

    return ""


print(destCity(paths))
