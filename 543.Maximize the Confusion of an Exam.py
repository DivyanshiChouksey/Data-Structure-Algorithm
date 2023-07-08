# Maximize the Confusion of an Exam

answerKey = "TTFTTFTT"
k = 1

def maxConsecutiveAnswers(answerKey, k) :
    left = 0
    ans = 0
    cntT = 0
    cntF = 0
    for i in range(len(answerKey)):
        if answerKey[i] == "T":
            cntT+=1
        else:
            cntF+=1
        while min(cntT,cntF) >k:       # reducing the window
            if answerKey[left] == "T":
                cntT-=1
            else:
                cntF-=1
            
            left+=1
        ans = max(ans,i-left+1)
    return ans

print(maxConsecutiveAnswers(answerKey,k))