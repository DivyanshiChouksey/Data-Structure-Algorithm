# Unique Morse Code Words
"""
    Creating a dictionary to map character to their signs and 
    a set to store unqiue morse code words
    and convert each and every character in each word to their sign and add it in set and 
    return length of set.
"""
# Time Complexity = O(m*n)   m=len(word) , n = len(words)
# Space Complexity = O(1)

words = ["gin", "zen", "gig", "msg"]


def uniqueMorseRepresentations(words):
    ans = set()
    for word in words:
        ans.add(convert(word))
    return len(ans)


def convert(word):
    dct = {
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
    }
    res = ""
    for i in range(len(word)):
        res += dct[word[i]]
    return res


# Solution2
"""
    Create an array of sign and go through the word in words and convert character of word 
    into sign through the index with help of ASCII and add it in a set and return length of set.
"""
# Time Complexity = O(m*n)|| Space Complexity = O(1)


def uniqueMorseRepresentations1(words):
    sign = [
        ".-",
        "-...",
        "-.-.",
        "-..",
        ".",
        "..-.",
        "--.",
        "....",
        "..",
        ".---",
        "-.-",
        ".-..",
        "--",
        "-.",
        "---",
        ".--.",
        "--.-",
        ".-.",
        "...",
        "-",
        "..-",
        "...-",
        ".--",
        "-..-",
        "-.--",
        "--..",
    ]
    ans = set()
    for word in words:
        tmp = ""
        for ch in word:
            tmp += sign[ord(ch) - ord("a")]
        ans.add(tmp)
    return len(ans)


print(uniqueMorseRepresentations(words))
print(uniqueMorseRepresentations1(words))
