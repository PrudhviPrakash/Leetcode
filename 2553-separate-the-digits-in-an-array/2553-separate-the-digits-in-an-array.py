class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        num=[]
        for i in  nums:
            num1=[]
            if i==0:
                num1.append(i)
            while i>0:
                num1.append(i%10)
                i//=10
            num.append(num1)
        num2=[]
        for i in range(len(num)):
            for j in range(len(num[i])-1,-1,-1):
                num2.append(num[i][j])
        return num2
                    


        