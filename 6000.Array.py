# Two Sum

nums = [2, 4, 6, 8, 1, 5]


def twoSum3(nums, target):
    dct = {}
    for i, num in enumerate(nums):
        if num in dct:
            return [dct[num], i]
        else:
            dct[target - num] = i


# Waterfall Stream (not hard but lenghty)

array = [
    [0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0],
]
source = 3


def waterfallStreams(array, source):
    aboveRow = array[0][:]
    aboveRow[source] = -1
    for i in range(1, len(array)):
        current = array[i][:]
        for j in range(len(aboveRow)):
            valueAbove = aboveRow[j]
            hasWater = valueAbove < 0
            hasBlock = current[j] == 1
            if not hasWater:
                continue
            if not hasBlock:
                current[j] += aboveRow[j]
                continue
            splitWater = valueAbove / 2
            right = j
            while right + 1 < len(aboveRow):
                right += 1
                if aboveRow[right] == 1:
                    break
                if current[right] != 1:
                    current[right] += splitWater
                    break

            left = j
            while left - 1 >= 0:
                left -= 1
                if aboveRow[left] == 1:
                    break
                if current[left] != 1:
                    current[left] += splitWater
                    break

        aboveRow = current
    return list(map(lambda x: x * -100, aboveRow))


print(waterfallStreams(array, source))


# ------------------------------------------------------------------------

# merge Interval

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]


def mergeInterval(intervals):
    sortedIntervals = sorted(intervals, key=lambda x: x[0])
    current = sortedIntervals[0]
    ans = []
    ans.append(current)
    for interval in sortedIntervals:
        curStart, curEnd = current
        nxtStart, nxtEnd = interval
        if curEnd >= nxtStart:
            current[1] = max(curEnd, nxtEnd)
        else:
            current = interval
            ans.append(current)

    return ans


print(mergeInterval(intervals))


# --------------------------------------------------------------


def valSubsequence(array, sequence):
    arrIdx, seqIdx = 0, 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)


print(valSubsequence([5, 1, 22, 6, 25, -1, 8, 10], [1, 6, -1, 10]))


# --------------------------------------------------------------------------
