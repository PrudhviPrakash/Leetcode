class Solution:
    def sumAndMultiply(self, n: int) -> int:
        l=[]
        s=0
        while n>0:
            a=n%10
            l.append(a)
            s+=a
            n//=10
        ans=0
        for i in range(len(l)-1,-1,-1):
            if l[i]!=0:
                ans=ans*10+l[i]
        return ans*s
