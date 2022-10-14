# Reverse Words In String

string = "AlgoExpert is the best!"


def reverseWordsInString(string):
    words = []
    startOfWord = 0
    for i in range(len(string)):
        character = string[i]
        if character == " ":
            words.append(string[startOfWord:i])
            startOfWord = i
        elif string[startOfWord] == " ":
            words.append(" ")
            startOfword = i

    words.append(string[startOfWord:])

    reverseList(words)
    return "".join(words)


def reverseList(list):
    start, end = 0, len(list) - 1
    while start < end:
        list[start], list[end] = list[end], list[start]
        start += 1
        end -= 1


print(reverseWordsInString(string))
