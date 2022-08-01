# Tournament Winner

"""
    Simply we have store the score board of competitions 
    for every competitions held we will make a record of winner teams with their scores
    and return the maximum scores winning team.
"""

competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
results = [0, 0, 1]

# Solution 1
# Time Complexity = O(n) || Space Complexity = O(n)
def tournamentWinner(competitions, results):
    scores = {}
    for team, winner in zip(competitions, results):
        if winner == 0:
            if team[1] not in scores:
                scores[team[1]] = 3
            else:
                scores[team[1]] += 3
        else:
            if team[0] not in scores:
                scores[team[0]] = 3
            else:
                scores[team[0]] += 3
    # return max(scores)
    ans = 0
    winner = ""
    for k, v in scores.items():
        if v >= ans:
            ans = v
            winner = k
    return winner


# Solution 2
# Time Complexity = O(n) || Space Complexity = O(n)
def tournamentWinner2(competitions, results):
    scores = {}
    for i, team in enumerate(competitions):
        if results[i] == 0:
            if team[1] not in scores:
                scores[team[1]] = 3
            else:
                scores[team[1]] += 3
        else:
            if team[0] not in scores:
                scores[team[0]] = 3
            else:
                scores[team[0]] += 3
    ans = 0
    winner = ""
    for k, v in scores.items():
        if v >= ans:
            ans = v
            winner = k
    return winner


# Solution 3
# Time Complexity = O(n) || Space Complexity = O(n)
def tournamentWinner3(competitions, results):
    scores = {}
    for i in range(len(competitions)):
        if results[i] == 0:
            if competitions[i][1] not in scores:
                scores[competitions[i][1]] = 3
            else:
                scores[competitions[i][1]] += 3
        else:
            if competitions[i][0] not in scores:
                scores[competitions[i][0]] = 3
            else:
                scores[competitions[i][0]] += 3
    ans = 0
    winner = ""
    for k, v in scores.items():
        if v >= ans:
            ans = v
            winner = k
    return winner


print(tournamentWinner(competitions, results))

print(tournamentWinner2(competitions, results))

print(tournamentWinner3(competitions, results))
