# Sort Integers by The Number of 1 Bits

arr = [0,1,2,3,4,5,6,7,8]
# output = [0,1,2,4,8,3,5,6,7]


def sortByBits(arr):
    def find_weight(num):
        mask = 1
        weight = 0
        
        while num:
            if num & mask:
                weight += 1
                num ^= mask
            
            mask <<= 1
        
        return weight
    
    arr.sort(key = lambda num: (find_weight(num), num))
    return arr


print(sortByBits(arr))
