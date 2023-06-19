# Find the Highest Altitude

gain = [-5,1,5,0,-7]

def largestAltitude(gain):
    tmp = ans = 0
    for num in gain:
        tmp+=num
        ans=max(ans,tmp)
    return ans
  
print(largestAltitude(gain))
