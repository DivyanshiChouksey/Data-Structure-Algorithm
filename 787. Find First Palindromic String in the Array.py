 # Find First Palindromic String in the Array

words = ["abc","car","ada","racecar","cool"]

def firstPalindrome(words):
    def isPalindrome(s):
        i, j = 0, len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    for word in words:
        if isPalindrome(word):
            return word
    return ""


print(firstPalindrome(words))

# solution 2

def firstPalindrome(words):
    for word in words:
        if word[::-1]== word:
            return word
    return ""

print(firstPalindrome(words))
    
