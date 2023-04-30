# Add Digits

# 4th Solution - using Formula
# Time - O(1) || Space - O(1)
num = 38 

def addDigits4(num):
    if num == 0:
        return 0
    if num % 9 == 0:
        return 9
    return num % 9
  
print(addDigits4(num))



# 3rd Solution - optimizing space as constant (without converting into string) 
# Time - O(n) || Space - O(1)
num = 38

def addDigits3(num):
    while True:
        ans = 0
        while num:
            ans +=num%10
            num//=10
        if ans//10==0:
            return ans
        num=ans
     
print(addDigits3(num))
    
  
  
# 2nd Solution - using Loop
# Time - O(n) || Space - O(n)
num 38

def addDigits2(num):
    while True:
        ans = 0
        for i in str(num):
            ans+=int(i)
        if ans in [0,1,2,3,4,5,6,7,8,9]: or ans//10==0
            return ans
        num=ans
    
 print(addDigits2(num))



# 1st Solution - using Recursion 
# Time - O(n) || Space - O(n)
num = 38

def addDigits(num):
    def helper(num):
        ans = 0
        for i in str(num):
            ans+=int(i)
        if ans in [0,1,2,3,4,5,6,7,8,9]:
            return ans
        return helper(ans)
      
    return helper(num)
  

print(addDigits(num))
