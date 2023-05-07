# Find the Longest Valid Obstacle Course at Each Position

obstacles = [1,2,3,2]

import bisect

def longestObstacleCourseAtEachPosition(obstacles):
    lis = []
    result = []
    for obstacle in obstacles:
        idx = bisect.bisect_right(lis, obstacle)
        if idx == len(lis):
            lis.append(obstacle)
        else:
            lis[idx] = obstacle
        result.append(idx+1)
    return result
  
print(longestObstacleCourseAtEachPosition(obstacles))
