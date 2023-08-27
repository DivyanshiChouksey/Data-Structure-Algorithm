# Frog Jump

stones = [0,1,3,5,6,8,12,17]


def canCross(stones):
    d = {}
    for i, s in enumerate(stones):
        d[s] = i

    visited = {(0,0)}

    q = [(0,0)]
    while q:
        pos, lastJump = q.pop()
        if pos == len(stones) - 1: return True
        for dx in [-1,0,1]:
            nextJump = lastJump + dx
            if nextJump <= 0: continue
            nextUnit = stones[pos]+nextJump
            if nextUnit in d:
                nextPos = d[nextUnit]
                if (nextPos, nextJump) in visited: continue
                visited.add((nextPos, nextJump))
                q.append( (nextPos, nextJump) )

    return False


print(canCross(stones))


