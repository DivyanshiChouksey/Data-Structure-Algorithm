# Group Anagrams

"""
    Here start with creating a hashmap so we can keep record of group of anagrams
    Go through the given array words and for each word Firstly sort it and store it in a variable
    and if sorted word is aleready in hashmap then append the word in it otherwise create new one
    at the end return the list of hashmaps values.
"""

# Time Complexity = O(n*w*log(n))
# space Complexity = O(wn)

words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]


def groupAnagrams(words):
    anagrams = {}
    for word in words:
        sortedWord = "".join(sorted(word))
        if sortedWord in anagrams:
            anagrams[sortedWord].append(word)
        else:
            anagrams[sortedWord] = [word]
        print(anagrams)
    return list(anagrams.values())


print(groupAnagrams(words))
