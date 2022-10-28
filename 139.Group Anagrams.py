# Group Anagrams

"""
    Here start with creating a hashmap so we can keep record of group of anagrams
    Go through the given array words and for each word Firstly sort it and store it in a variable
    and if sorted word is aleready in hashmap then append the word in it otherwise create new one
    at the end return the list of hashmaps values.
"""

# Time Complexity = O(n*w*log(n)) , n = len(words)
# space Complexity = O(wn)        , w = len(average word) "each word"

words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]


def groupAnagrams(words):
    anagrams = {}
    for word in words:
        sortedWord = "".join(sorted(word))
        if sortedWord in anagrams:
            anagrams[sortedWord].append(word)
        else:
            anagrams[sortedWord] = [word]
    return list(anagrams.values())


# Solution 2

"""
    Go through the given array words and for each word instead of storing sorted Word as key in hashmap 
    we use count of frequency of each character in word and (eg :- "eat" --> count(e-1,a-1,t-1))
    store it as key so that we don't need to sort the word
    if count is aleready in hashmap then append the word in it otherwise create new one,
    at the end return the list of hashmaps values.
"""

# Time Complexity = O(n.m)  , n = len(words)
# Space Complexity = O(n.m) , m = len(average word) "each word"

from collections import defaultdict


def groupAnagrams2(words):
    dct = defaultdict(list)

    for word in words:
        count = [0] * 26
        for ch in word:
            count[ord(ch) - ord("a")] += 1

        dct[tuple(count)].append(word)

    return dct.values()


print(groupAnagrams(words))
print(groupAnagrams2(words))
