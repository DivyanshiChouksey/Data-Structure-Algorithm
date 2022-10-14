garbage = ["G", "P", "GP", "GG"]
travel = [2, 4, 3]
pref = [0] * (len(travel) + 1)
for i, ti in enumerate(travel):
    pref[i + 1] = pref[i] + ti
# print(pref) -> 0,2,6,9
ans = sum(map(len, garbage))

for c in "GMP":
    idx = 0
    for i, gi in enumerate(garbage):
        idx = i if c in gi else idx
    ans += pref[idx]
