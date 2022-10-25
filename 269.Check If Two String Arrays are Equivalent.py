# Check If Two String Arrays are Equivalent

# Optimal Solution
"""
    Taking 4 pointer, Two for keep track of current word in word1 and word2 (i1, i2)
    and another Two for keep record of current character in current word of word1 and word2 (j1, j2) then after
    we check for our pointers to be inside our array and when they finish one string we move them to next string in array
    NOTE :- we can have different size of array so we check that they stay inside len of array 

    we can do that by following these steps , go through the both array using while loop and check 
    1. if current character is not equal then return False (word1[i1][j1] != word2[i2][j2])
    2. if j1 == len(word1[i1] then move pointer to next word i1+=1 and make j1=0
    3. similarly check j2 == len(word2[i2] then move pointer to next word i2+=1 and make j2=0
    4. if i1 and i2 == len of both arrays respetively then return True 

"""
# Time Complexity = O(min(len of character of word1 and word2))
# Space Complexity = O(1)
word1 = ["ab", "c"]
word2 = ["a", "bc"]


def arrayStringsAreEqual(word1, word2):
    i1 = j1 = i2 = j2 = 0
    while i1 < len(word1) and i2 < len(word2):
        if word1[i1][j1] != word2[i2][j2]:
            return False
        j1 += 1
        j2 += 1

        if j1 == len(word1[i1]):
            i1 += 1
            j1 = 0
        if j2 == len(word2[i2]):
            i2 += 1
            j2 = 0

        if i1 == len(word1) and i2 == len(word2):
            return True

    return False


# Naive Solution
"""
    Concatenate each word of word1 and store it
    similarly concatinate each word of word2 and store it then
    return True if w1 and w2 are equal else return False   
"""
# Time Complexity = O(min(n,m)) , n = len(w1)
# Space Complexity = O(n+m)     , m = len(w2)

word1 = ["ab", "c"]
word2 = ["a", "bc"]


def arrayStringsAreEqual2(word1, word2):
    w1 = "".join(word1)
    w2 = "".join(word2)
    return w1 == w2


print(arrayStringsAreEqual(word1, word2))
print(arrayStringsAreEqual2(word1, word2))
