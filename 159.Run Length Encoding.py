# Run Length Encoding
"""
    Instead of taking a empty string taking an array to store encoded String Characters so that we can reduce runtime
    iterating through the string and keeping the record of current length of same character along with keep in mind
    if current length is equals to 9 then append the length and the character and again start counting legth from 1
    for edge cases i==len(string) then no need to compare char only just append the length and the character   
    at last return array as string.
"""

# Time Complexity = O(n) || Space Complexity = O(n)

string = "AAAAAAAAAAAAABBCCCCDD"


def runLengthEncoding(string):
    encodedStringCharacters = []
    currentRunLength = 1

    for i in range(1, len(string)):
        # currentCharacter = string[i]
        # prev = string[i-1]
        if string[i] != string[i - 1] or currentRunLength == 9:
            encodedStringCharacters.append(str(currentRunLength))
            encodedStringCharacters.append(string[i - 1])
            currentRunLength = 0
        currentRunLength += 1

    encodedStringCharacters.append(str(currentRunLength))
    encodedStringCharacters.append(string[len(string) - 1])

    return "".join(encodedStringCharacters)


print(runLengthEncoding(string))
