# Task Assignment

# Time Complexity = O(nlogn) || Space Complexity = O(n)
k = 3
tasks = [1, 3, 5, 3, 1, 4]  #  1,1,3,3,4,5


def taskAssignment(k, tasks):
    pairedTask = []
    dct = getIdx(tasks)
    sortedTask = sorted(tasks)

    for i in range(k):
        task1 = sortedTask[i]
        duration = dct[task1]
        t1idx = duration.pop()

        task2 = sortedTask[len(tasks) - 1 - i]
        duration2 = dct[task2]
        t2idx = duration2.pop()

        pairedTask.append([t1idx, t2idx])

    return pairedTask


def getIdx(tasks):
    dct = {}
    for idx, task in enumerate(tasks):
        if task in dct:
            dct[task].append(idx)
        else:
            dct[task] = [idx]
    print(dct)
    return dct


print(taskAssignment(k, tasks))
