# Minimum Characters for Words
"""
    Start with an empty dictionary to store max frequencies of required word's character
    go through every word of words and then count the frequencies of every character and then update maxfreq
    after that make an array with all char of dict repeated freq time   
"""

# Time Complexity = O(n*l),  n=len(words) , l = length of the longest word
# Space Complexity = O(c),   c=no. of unique char

words = ["this", "that", "did", "deed", "them!", "a"]


def minimumCharactersForWords(words):
    maxCharFreq = {}
    for word in words:
        frequencies = countFreq(word)
        updateMaxFreq(frequencies, maxCharFreq)
    return makeArray(maxCharFreq)


def countFreq(string):
    frequencies = {}
    for ch in string:
        if ch in frequencies:
            frequencies[ch] += 1
        else:
            frequencies[ch] = 1
    return frequencies


def updateMaxFreq(frequencies, maxCharFreq):
    for ch in frequencies:
        if ch in maxCharFreq:
            maxCharFreq[ch] = max(frequencies[ch], maxCharFreq[ch])
        else:
            maxCharFreq[ch] = frequencies[ch]


def makeArray(maxCharFreq):
    character = []
    for ch in maxCharFreq:
        for _ in range(maxCharFreq[ch]):
            character.append(ch)

    return character


print(minimumCharactersForWords(words))
