class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d={}
        st=""      
        for i in t:
            d[i]=d.get(i,0)+1
        for i in s:
            if i in d:
                d[i]=d[i]-1
        print(d)
        for i in d:
            if d[i]!=0:
                st+=i
        return st

