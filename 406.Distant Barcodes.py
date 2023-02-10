# Distant Barcodes

"""
    Find highest frequency element and arrange it on ans[0], ans[2], ans[4]..
    then the next highest frequency element is arranged it on ans[1], ans[3], and so on..

    Hint - can do these step by taking a pointer i=0 then place value and increase it by i+=2 
           use - most_common() function to find highest frequency elements in Counter
"""

# Time Complexity = O(n) || Space Complexity = O(n)

from collections import Counter

barcodes = [1,1,1,1,2,2,3,3]

def rearrangeBarcodes(barcodes):
    ans = [0]*len(barcodes)
    freq = Counter(barcodes).most_common()
    # print(freq)
    i=0
    for k,v in freq:
        for _ in range(v):
            ans[i]= k
            i+=2
            if i>=len(barcodes):
                i=1
    return ans

print(rearrangeBarcodes(barcodes))