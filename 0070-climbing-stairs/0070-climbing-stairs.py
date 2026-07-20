class Solution:
    def climbStairs(self, n: int) -> int:
        l=[-1]*(n+1)
        def climb(n,l):
            if n<=1:
                return 1
            if l[n]!=-1:
                return l[n]
            l[n]=climb(n-1,l)+climb(n-2,l)
            return l[n]
        return climb(n,l)

        