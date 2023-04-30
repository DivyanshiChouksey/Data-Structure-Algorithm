# Similar String Groups

strs = ["tars","rats","arts","star"]

def numSimilarGroups(strs):
    if not strs: return 0

    def dist(s, t):
        d = 0
        for a, b in zip(s, t):
            if a != b:
                d += 1
        return d

    visited = set()
    q = collections.deque()
    count = 0
    for i in range(len(strs)):
        # perform a bfs on every s in strs
        if strs[i] in visited:
            continue

        q.append(strs[i])
        count += 1
        while q:
            curr = q.popleft()
            visited.add(curr)

            # find neighbors with edit dist of 2
            for s in strs:
                if s not in visited and dist(curr, s) == 2:
                    q.append(s)

    return count
  
print(numSimilarGroups(strs))
