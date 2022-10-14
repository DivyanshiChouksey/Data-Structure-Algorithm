from collections import defaultdict


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

if endWord not in wordList:
    # return 0
    pass
wordList.append(beginWord)
neighbor = defaultdict(list)

for word in wordList:
    for i in range(len(word)):
        pattern = word[:i] + "#" + word[i + 1 :]  # pattern = #ot, word = hot
        neighbor[pattern].append(word)
print(neighbor)
# hit -> #it,h#t,hi#
# hot->
# lot, dot ->
# visited = set(beginWord)
# queue = [beginWord]
# ans = 1
# while queue:
#     for i in range(len(queue)):
#         word = queue.pop(0) # popleft
