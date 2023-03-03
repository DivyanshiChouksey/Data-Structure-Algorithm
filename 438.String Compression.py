# String Compression

"""
    Using sliding window approach and for optimization modifying the input array
    taking two pointer i, j initially at 0th index then by using sliding window count the 
    group of consecutive repeating characters after that first place the character by updating chars[i] = chars[j]
    and then for count check if count is bigger than 1 then at (i+1)th indeces 
    update the character with the count (digit by digit) of ith indexed character else if count is 1 then 
    place it at the jth index and move to the next at the end return the index of i for the length of compressed 
    string.

Note - compressing the string and updating it inplace from 0th index
       example:-                                 i                                    j
                            ["a","a","a""b","b","b","b","b","b","b","b","b","b","b","b"]
                              0   1   2  3   4   5   6   7
                compressed str - ["a","3","b","1","2"]

                length of compressed string would be 5
"""

# Time Complexity = O(n) || Space Complexity = O(1)

chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

def compress(chars):
    i=0
    j=0
    while j<len(chars):
        chars[i] = chars[j]
        count = 1
        while j+1<len(chars) and chars[j]==chars[j+1]:
            j+=1
            count+=1
        if count>1:
            for digit in str(count):
                chars[i+1] = digit
                i+=1

        j+=1
        i+=1
    return i

print(compress(chars))