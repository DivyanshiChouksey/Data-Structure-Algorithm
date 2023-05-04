# Dota2 Senate

senate = "RDDDRDRRDR"

def predictPartyVictory(senate):
    n = len(senate)
    r_que = deque()
    d_que = deque()

    for i in range(len(senate)):
        if senate[i]=="R":
            r_que.append(i)
        else:
            d_que.append(i)

    while r_que and d_que:
        i = r_que.popleft()
        j = d_que.popleft()

        if i<j:
            r_que.append(n+1)
        else:
            d_que.append(n+1)
        n+=1

    return "Radiant" if len(d_que)==0 else "Dire"
  
  
  
print(predictPartyVictory(senate))
