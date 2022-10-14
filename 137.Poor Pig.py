# Poor Pigs

buckets = 4
minutesToDie = 15
minutesToTest = 15


def poorPigs(buckets, minutesToDie, minutesToTest):
    pigs = 0
    while (minutesToTest / minutesToDie + 1) ** pigs < buckets:
        pigs += 1
    return pigs


print(poorPigs(buckets, minutesToDie, minutesToTest))
