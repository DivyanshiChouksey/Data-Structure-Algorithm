# 1. Minimum Waiting Time
"""
    Greedy Approach 
    The idea behind this is we need to figure out that executing shortest queries first is all
    will lead to the minimum Waiting Time becuase all the queries after it,
    again will wait minimum amount of time before they're executing (Sorting).
"""
# Time Complexity = O(nlogn) || Space Complexity = O(1)

queries = [6, 1, 3, 2, 2]


def minimumWaitingTime(queries):
    queries.sort()
    ans = 0
    for i, time in enumerate(queries):
        lefted = len(queries) - (i + 1)
        ans += time * lefted
    return ans


print(minimumWaitingTime(queries))


# ----------------------------------------------------------------------------------------------------------------------------

# 2. Class Photos

# Time Complexity =O(nlogn) || Space Complexity = O(1)

red = [5, 8, 1, 3, 4]
blue = [6, 9, 2, 4, 5]


def classPhotos(red, blue):
    red.sort(reverse=True)
    blue.sort(reverse=True)

    frontRow = "RED" if red[0] < blue[0] else "BLUE"
    for i in range(len(red)):
        if frontRow == "RED":
            if red[i] >= blue[i]:
                return False
        else:
            if blue[i] >= red[i]:
                return False
    return True


print(classPhotos(red, blue))


# ----------------------------------------------------------------------------------------------------------------------------

# 3. Tandem Cycle

# Time Complexity =O(nlogn) || Space Complexity = O(1)


red = [5, 5, 3, 9, 2]  # 2,3,5,5,9
blue = [3, 6, 7, 2, 1]
fastest = True


def tandemBicycle(red, blue, fastest):
    red.sort()
    blue.sort()

    if not fastest:
        red.sort(reverse=True)

    i = 0
    j = len(blue) - 1
    ans = 0
    while i < len(red) and j >= 0:
        ans += max(red[i], blue[j])
        i += 1
        j -= 1
    return ans


print(tandemBicycle(red, blue, fastest))

# ----------------------------------------------------------------------------------------------------------------------------

# 4. Task Assignment

# Time Complexity =O(nlogn) || Space Complexity = O(1)

k = 3
tasks = [1, 3, 5, 3, 1, 4]


def taskAssignment(k, tasks):
    dct = getsPairs(tasks)
    sortedtask = sorted(tasks)
    paired = []

    for i in range(k):
        tasks1 = sortedtask[i]
        duration = dct[tasks1]
        t1idx = duration.pop()

        task2 = sortedtask[len(tasks) - 1 - i]
        duration2 = dct[task2]
        t2idx = duration2.pop()

        paired.append([t1idx, t2idx])

    return paired


def getsPairs(tasks):
    dct = {}
    for i, task in enumerate(tasks):
        if task in dct:
            dct[task].append(i)
        else:
            dct[task] = [i]

    return dct


print(taskAssignment(k, tasks))

# ---------------------------------------------------------------------------------------
