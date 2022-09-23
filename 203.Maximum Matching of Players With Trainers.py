# Maximum Matching of Players With Trainers
"""
    Greedy Approach
    sort both the array and start from the end in both array and if player is less than or equals to trainer 
    that means player's ability is less than or equal to the trainer's training capacity and increase match by one
    and return match.
"""
# Time Complexity = O() || Space Complexity = O()
players = [4, 7, 9]
trainers = [8, 2, 5, 8]


def matchPlayersAndTrainers(players, trainers):
    players.sort()
    trainers.sort()
    count = 0
    i = len(players) - 1
    j = len(trainers) - 1
    while i >= 0 and j >= 0:
        while i >= 0 and j >= 0 and players[i] <= trainers[j]:
            count += 1
            i -= 1
            j -= 1
        i -= 1
    return count


print(matchPlayersAndTrainers(players, trainers))
