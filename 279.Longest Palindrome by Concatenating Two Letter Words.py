# Longest Palindrome by Concatenating Two Letter Words

from collections import Counter

# Solution 1

a = ["lc", "cl", "gg"]


def longestPalindrome(a):
    wc = Counter(a)
    aa = 0  # count how many words contain only two identical letters like 'aa'
    center = 0  # if one count of 'aa' is odd, that means it can be the center of the palindrome, answer can plus 2
    abba = 0  # count how many word pairs like ('ab', 'ba') and they can put on both sides respectively

    for w, c in wc.items():
        if w[0] == w[1]:  # like 'aa', 'bb', ...
            aa += (
                c // 2 * 2
            )  # if there are 3 'aa', we can only use 2 'aa' put on both sides respectively
            # if one count of 'aa' is odd, that means it can be the center of the palindrome, answer can plus 2
            if c % 2 == 1:
                center = 2
        else:
            abba += min(wc[w], wc[w[::-1]]) * 0.5  # will definitely double counting
    return aa * 2 + int(abba) * 4 + center


print(longestPalindrome(a))

# Solution 2

words = ["lc", "cl", "gg"]


def longestPalindrome(a):
    count = Counter(words)
    answer = 0
    central = False
    for word, count_of_the_word in count.items():
        # if the word is a palindrome
        if word[0] == word[1]:
            if count_of_the_word % 2 == 0:
                answer += count_of_the_word
            else:
                answer += count_of_the_word - 1
                central = True
        elif word[0] < word[1]:
            answer += 2 * min(
                count_of_the_word, count[word[1] + word[0]]
            )  # count[ab],count[ba]
    if central:
        answer += 1

    return 2 * answer


print(longestPalindrome(words))
