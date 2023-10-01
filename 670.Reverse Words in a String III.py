# Reverse Words in a String III

s = "Let's take LeetCode contest"


def reverseWords(s) :
    ans = []
    s2 = s.split(" ")
    # print(s2)
    for word in s2:
        ans.append(word[::-1])
    # print(ans)
    return " ".join(ans)

print(reverseWords(s))


s = "Let's take LeetCode contest"

def reverseWords(s):
    i = 0
    j = 0
    ans = ""
    while j<len(s):
        while j<len(s) and s[j] != " ":
            j+=1
        tmp = s[i:j]
        ans+=tmp[::-1]
        if j!=len(s):
            ans+=s[j]
        j+=1
        i=j
    return ans
