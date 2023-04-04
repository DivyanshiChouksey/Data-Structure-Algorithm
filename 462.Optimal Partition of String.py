# Optimal Partition of String

class Solution:
    def partitionString(self, s: str) -> int:
        ans=0
        tmp=set()
        for i in range(len(s)):
            if s[i] in tmp :
                # ans.append(tmp)
                ans+=1
                tmp=set()
                tmp.add(s[i])
            else:
                tmp.add(s[i])
        # print(ans,tmp)
        # ans.append(tmp)
        return ans+1
