#  Check if the Sentence Is Pangram

sentence = "thequickbrownfoxjumpsoverthelazydog"


# Solution 1
"""
    Make set of given sentence and check if length of set is "26"
    return True else False
"""
# Time Complexity = O(n) || Space Complexity = O(1)


def checkIfPangram(sentence) -> bool:
    return len(set(sentence)) == 26


# Solution 2
"""
    So we make a 26 space array initially initializing with 0
    then keep track of character in array using ord function after that 
    if any one of value in array is zero then return False else return True 
"""
# Time Complexity = O(n) || Space Complexity = O(1)


def checkIfPangram2(sentence) -> bool:
    array = [0 for i in range(26)]
    # print(array)
    for i in range(len(sentence)):
        array[ord(sentence[i]) - ord("a")] += 1

    # print(array)
    for ele in array:
        if ele == 0:
            return False

    return True


print(checkIfPangram(sentence))
print(checkIfPangram2(sentence))
