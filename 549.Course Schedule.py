# Course Schedule


numCourses = 2
prerequisites = [[1,0]]


def canFinish(numCourses, prerequisites) :
    map = {i: [] for i in range(numCourses)}
    for course, pre in prerequisites:
        map[course].append(pre)

    toVisit = set()


    def dfs(node):
        if node in toVisit:
            return False
        if map[node] == []:
            return True
        toVisit.add(node)
        for sub in map[node]:
            if not dfs(sub):
                return False
        toVisit.remove(node)
        map[node] = []
        return True


    for i in range(numCourses):
        if not dfs(i):
            return False
    return True
