# Maximum Length of a Concatenated String with Unique Characters

arr = ["un","iq","ue"]

def maxLength(arr):
    dp = [set()]
    for a in arr:
        if len(set(a)) < len(a): continue
        a = set(a)
        for c in dp[:]:
            if a & c: continue
            dp.append(a | c)

    return max(len(a) for a in dp)


print(maxLength(arr))
