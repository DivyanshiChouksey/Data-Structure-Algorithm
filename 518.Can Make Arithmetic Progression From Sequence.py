# Can Make Arithmetic Progression From Sequence

arr = [3,5,1]

def canMakeArithmeticProgression(arr):
    arr.sort()
    r = arr[1] - arr[0]
    tmp = arr[0]
    for num in arr[1:]:
        tmp += r
        if tmp != num:
            return False
    return True
  
print(canMakeArithmeticProgression(arr))
