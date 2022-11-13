# Reverse Words in a String

s = "  hello world  "


def reverseWords(s):
    return " ".join(s.strip().split()[::-1])


print(reverseWords(s))
