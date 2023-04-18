# Merge Strings Alternately

word1 = "ab"
word2 = "pqrs"

# Solution 1
def mergeAlternately1(word1, word2):
  i = j = 0
  ans = ""
  while i<len(word1) and j<len(word2):
      ans += word1[i]
      ans += word2[j]
      i+=1
      j+=1

  if i==len(word1):
      ans+=word2[j:]
  else:
      ans+=word1[i:]

  return ans

# Solution 2
def mergeAlternately2(word1, word2):
  i=0
  ans = ""
  for word in word1:
      ans += word
      if i < len(word2):
          ans += word2[i]
          i+=1

  if i!= len(word2):
      ans+=word2[i:]
  return ans


# Solution 3
def mergeAlternately3(word1, word2):
  ans = ""
  for i,j in zip(word1,word2):
      ans+=i
      ans+=j
  if len(word1)>len(word2):
      ans+=word1[len(word2):]
  if len(word1)<len(word2):
      ans+=word2[len(word1):]
  return ans


print(mergeAlternately1(word1, word2))
print(mergeAlternately2(word1, word2))
print(mergeAlternately3(word1, word2))
