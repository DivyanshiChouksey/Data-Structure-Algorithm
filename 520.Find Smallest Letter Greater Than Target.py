# Find Smallest Letter Greater Than Target

letters = ["c","f","j"]
target = "a"

def nextGreatestLetter(letters, target):
    i = 0
    j = len(letters)-1
    while i<=j:
        mid = (i+j)//2
        if letters[mid] <= target:
            i = mid + 1
        else:
            j = mid - 1

    if i == len(letters):
        return letters[0]

    return letters[i]
  
print(nextGreatestLetter(letters, target))
