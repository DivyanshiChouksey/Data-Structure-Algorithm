#  Maximum Number of Events That Can Be Attended II


events = [[1,2,4],[3,4,3],[2,3,1]]
k = 2


def maxValue( events, k):        
    events.sort()
    n = len(events)
    starts = [start for start, end, value in events]
    dp = [[-1] * n for _ in range(k + 1)]
    
    def dfs(cur_index, count):
        if count == 0 or cur_index == n:
            return 0
        if dp[count][cur_index] != -1:
            return dp[count][cur_index]

        # Find the nearest available event after attending event 0.

        next_index = bisect_right(starts, events[cur_index][1])
        dp[count][cur_index] = max(dfs(cur_index + 1, count), events[cur_index][2] + dfs(next_index, count - 1))
        return dp[count][cur_index]
    
    return dfs(0, k)

print(maxValue( events, k))
