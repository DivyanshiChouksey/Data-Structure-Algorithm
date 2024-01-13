#  Minimum Number of Steps to Make Two Strings Anagram

s = "bab"
t = "aba"


def minSteps(s, t):
    smp = {}
    tmp = {}
    cnt = 0

    for a in s:
        smp[a] = smp.get(a, 0) + 1

    for a in t:
        tmp[a] = tmp.get(a, 0) + 1

    for key, value in smp.items():
        if key in tmp:
            if value == tmp[key]:
                cnt += value
            else:
                cnt += min(value, tmp[key])

    return len(s) - cnt



print( minSteps(s, t))
