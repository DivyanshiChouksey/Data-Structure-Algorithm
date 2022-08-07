# Generate Document
"""
    Starting with an empty dictionary to maintain record of character in characters along with their frequencies
    and check whether every character in document is in dctionary with greater or equal frequencies 
    if character is in dct then reduce its frequency by one and repeat the process again and again
    lastly if we pass document without any fail then return True else Return False.
"""

# Time Complexity = O(n+m)  , n = len(characters) and m = len(document)
#  Space Complexity = O(n)

characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"


def generateDocument(characters, document):
    frequencies = {}
    for character in characters:
        if character not in frequencies:
            frequencies[character] = 0

        frequencies[character] += 1

    for character in document:
        if character not in frequencies or frequencies[character] == 0:
            return False

        frequencies[character] -= 1
    return True


print(generateDocument(characters, document))
