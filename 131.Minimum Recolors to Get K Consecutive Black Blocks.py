# Minimum Recolors to Get K Consecutive Black Blocks
blocks = "WBBWWBBWBW"
k = 7


def minimumRecolors(blocks, k):
    maxBlocks = 0
    for i in range(len(blocks) - k + 1):
        b = blocks[i : i + k].count("B")
        if b >= k:
            return 0
        maxBlocks = max(b, maxBlocks)
    return k - maxBlocks


print(minimumRecolors(blocks, k))
