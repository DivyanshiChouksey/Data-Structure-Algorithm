# Word Subsets
"""
    For each word in words2 keep a counter and keep max frequence of each character in words2 and also do that
    for each word in words1 and check if the value of the character in tmp counter is greater than or equals 
    to the value of the character in cnt counter then
    append the word in our ans.

"""
# Time Complexity = O(N+M)      N = total char in words1 , M = total char in words2
# Space Complexity = O(n+m)     n = len(words2) , m = len(words1)

words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["lo", "eo"]


from typing import Counter


def wordSubsets(words1, words2):
    cnt = Counter(words2[0])
    for word in words2[1:]:
        tmp = Counter(word)
        for k, v in tmp.items():
            cnt[k] = max(cnt[k], v)  # will count frequency of all char
    # print(cnt)
    ans = []
    for word in words1:
        tmp = Counter(word)
        found = True
        for k, v in cnt.items():
            if tmp[k] < v:
                found = False
                break
        if found:
            ans.append(word)
    return ans


print(wordSubsets(words1, words2))
