class Solution:
    def alternateDigitSum(self, n: int) -> int:
        num=[]
        while n>0:
            num.append(n%10)
            n//=10
        num.reverse()
        s=0
        for i in range(len(num)):
            if i%2==0:
                s+=num[i]
            else:
                s-=num[i]
        return s

        