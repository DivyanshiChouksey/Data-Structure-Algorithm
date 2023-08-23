# Reorganize String

s="aaabbaadef"


def reorganizeString(s):
    """ 
    s=aaabbaadef
    a=5
    b=2
    d=1
    e=1
    f=1

    ans = [a, b, a, b, a, d, a, e, a, f] 
    """
    count = Counter(s)
    freq = sorted(count.items(),key=lambda x:-x[1])

    if freq[0][1] >= (len(s)/2) +1:
        return ""

    ans = ["" for i in range(len(s))]

    i=0
    for k,v in freq:
        for j in range(v):
            ans[i] = k
            i+=2
            if i >=len(s):
                i=1

    return "".join(ans)


print(reorganizeString(s))
