# Disk Stacking


disks = [
  [2, 1, 2],
  [3, 2, 3],
  [2, 2, 8],
  [2, 3, 4],
  [1, 3, 1],
  [4, 4, 5]
]


def diskStacking(disks):
    disks.sort(key=lambda x:x[2])
    height = [disk[2] for disk in disks]
    seq = [None for disk in disks]
    maxHeight = 0
    for i in range(1,len(disks)):
        for j in range(0,i):
            if disks[j][0] < disks[i][0] and disks[j][1] < disks[i][1] and disks[j][2] < disks[i][2]:
                if height[i]<= disks[i][2]+height[j]:
                    height[i] = disks[i][2]+height[j]
                    seq[i] = j
        if height[i]>= height[maxHeight]:
            maxHeight = i

    return buildSeq(disks,seq,maxHeight)

def buildSeq(array , seq, currIdx):
    sequence = []
    while currIdx is not None:
        sequence.append(array[currIdx])
        currIdx = seq[currIdx]

    return list(reversed(sequence))

print(diskStacking(disks))

