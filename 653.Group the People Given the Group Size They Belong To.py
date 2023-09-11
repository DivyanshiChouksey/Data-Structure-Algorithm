# Group the People Given the Group Size They Belong To

# Time : O(n) 
# Space : O(n)

groupSizes = [3,3,3,3,3,1,3]


def groupThePeople(groupSizes):
    dct = defaultdict(list)
    for i in range(len(groupSizes)):
        dct[groupSizes[i]].append(i)

    ans = []
    for k,v in dct.items():
        # todo
        tmp = []
        for i in v:
            tmp.append(i)
            if len(tmp) == k:
                ans.append(tmp)
                tmp = [] 

    return ans 


print(groupThePeople(groupSizes))
