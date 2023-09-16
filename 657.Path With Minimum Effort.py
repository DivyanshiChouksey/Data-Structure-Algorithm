# Path With Minimum Effort

# heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]

heights = [[1,2,2],[3,8,2],[5,3,5]]

def minimumEffortPath(heights):
    # we should go little greedy
    n = len(heights)
    m = len(heights[0])

    dist = [[float('inf')] * m for _ in range(n)]
    dist[0][0] = 0

    pq = [(0, 0, 0)]  # (effort, row, col)

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    while pq:
        diff, row, col = heapq.heappop(pq)

        if row == n - 1 and col == m - 1:
            return diff

        for i in range(4):
            newr = row + dr[i]
            newc = col + dc[i]

            if 0 <= newr < n and 0 <= newc < m:
                newEffort = max(abs(heights[row][col] - heights[newr][newc]), diff)

                if newEffort < dist[newr][newc]:
                    dist[newr][newc] = newEffort
                    heapq.heappush(pq, (newEffort, newr, newc))

    return 0


print( minimumEffortPath(heights))
