# Count Days Spent Together

arriveAlice = "08-15"
leaveAlice = "08-18"
arriveBob = "08-16"
leaveBob = "08-19"


def countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob):
    dayspermm = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    aa = sum(dayspermm[: int(arriveAlice[:2]) - 1]) + int(arriveAlice[3:])
    la = sum(dayspermm[: int(leaveAlice[:2]) - 1]) + int(leaveAlice[3:])
    ab = sum(dayspermm[: int(arriveBob[:2]) - 1]) + int(arriveBob[3:])
    lb = sum(dayspermm[: int(leaveBob[:2]) - 1]) + int(leaveBob[3:])

    alice = set(range(aa, la + 1))
    bob = set(range(ab, lb + 1))

    return len(bob.intersection(alice))


print(countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob))
