# Combinations

n = 4
k = 2


def combine(n, k):
    ans=[]
    
    def helper(arr,path):
        if len(path)==k: 
            ans.append(path)
            return
        for i in range(len(arr)):
            helper(arr[i+1:],path+[arr[i]])
    
    helper(list(range(1,n+1)),[])
    return ans


print(combine(n, k))
