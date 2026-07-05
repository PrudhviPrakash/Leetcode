class Solution:
    def reverseVowels(self, s: str) -> str:
        l1=['a','e','i','o','u','A','E','I','O','U']
        s1=list(s)
        f=0
        l=len(s1)-1        
        while f<l:
            if s1[f] in l1 and s1[l] in l1:
                s1[f],s1[l]=s1[l],s1[f]
                f+=1
                l-=1
            elif s1[f] not in l1:
                f+=1
            else:
                l-=1
        a="".join(s1)
        return a

        