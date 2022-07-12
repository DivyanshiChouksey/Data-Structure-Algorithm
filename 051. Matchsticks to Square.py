# Matchsticks to Square
"""
    for this we do backtracking 
    we start keeping track of used sticks and then check them one by one 
    we are doing a DFS with memomization
    cheat is to sort the array in reverse order
"""



matchsticks = [1,1,2,2,2]

def makesquare(matchsticks):
    a = sum(matchsticks)
    if a%4 != 0:
        return False
    target = a/4
    used = [False]* len(matchsticks)
    matchsticks.sort(reverse = True)
    k = 4
    def backTracking(i,k,subSetSum):
        if k == 0: # BASE CASE
            return True
        if subSetSum == target:
            return backTracking(0,k-1,0)
        for j in range(i,len(matchsticks)):
            if used[j] or subSetSum + matchsticks[j] > target or (j > 0 and matchsticks[j] == matchsticks[j-1] and not used[j-1]):
                continue
            used[j] = True
            if backTracking(j+1,k,subSetSum+matchsticks[j]):
                return True
            used[j] = False
        return False
 
    return backTracking(0,k,0)

print(makesquare(matchsticks))