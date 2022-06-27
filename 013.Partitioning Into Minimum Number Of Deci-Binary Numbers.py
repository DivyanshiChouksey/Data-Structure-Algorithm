# Partitioning Into Minimum Number Of Deci-Binary Numbers
"""
    find tricky mathematical approach and smart solution

    n = "82734"
    n = "82734" (-11111)
         71623  (-11111)
         60512  (-10111)
         50401  (-10101)
         40300  (-10100)
         30200  (-10100)
         20100  (-10100)
         10000  (-10000)
         00000  

    # Approach (sometimes time limit exceeds)

    n = list(map(int ,n))
    count = 0
    while n != []:
        i = 0
        k = len(n)
        while i < k:        
            n[i] -= 1
            if n[i] == 0:
                n.pop(i)
                k -= 1
            else:
                i += 1
        count += 1
    print(count)
"""
# Time Complexity = O(n) || Space Complexity = O(1)


n = "82734"
# best Solution
def minPartitions(n):
    return max(n)

print(minPartitions(n))