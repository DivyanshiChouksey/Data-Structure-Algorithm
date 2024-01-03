# Number of Laser Beams in a Bank

bank = ["011001","000000","010100","001000"]

def numberOfBeams(bank):
    ans = prev = 0
    for s in bank:
        c = s.count('1')
        if c:
            ans += prev * c
            prev = c
    return ans


print(numberOfBeams(bank))
