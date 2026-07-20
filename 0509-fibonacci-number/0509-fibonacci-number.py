class Solution:
    def fib(self, n: int) -> int: 
        def fibb(n,l):
            if n<=1:
                l[n]=n
                return l[n]
            if l[n]!=-1:
                return l[n]
            l[n]=fibb(n-1,l)+fibb(n-2,l)
            return l[n]
        l=[-1]*(n+1)
        return fibb(n,l)  
        