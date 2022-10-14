# First Non-Repeating Character

string = "abcdcaf"

# Time Complexity = O(n^2) || Space Complexity = O(1)
def firstNonRepeatingCharacter(string):
    for i in range(len(string)):
        found = False
        for j in range(1, len(string)):
            if string[i] == string[j] and i != j:
                found = True

        if not found:
            return i
    return -1


# Time Complexity = O(n) || Space Complexity = O(1)
def firstNonRepeatingCharacter2(string):
    frequencies = {}
    for character in frequencies:
        if character in frequencies:
            frequencies[character] += 1
        else:
            frequencies[character] = 1

    for i in range(len(string)):
        if frequencies[string[i]] == 1:
            return i
    return -1


print(firstNonRepeatingCharacter(string))
print(firstNonRepeatingCharacter2(string))
