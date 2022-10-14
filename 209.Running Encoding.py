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
