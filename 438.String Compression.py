# String Compression

"""
    Using sliding window to count the frequency and make inplace change in chars array
    at i+1 index and for next character do the same at sequence indeces. 
"""

# Time Complexity = O(n) || Space Complexity = O(1)

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