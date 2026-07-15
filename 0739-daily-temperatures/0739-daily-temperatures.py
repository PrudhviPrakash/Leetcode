class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st=[]
        d={}
        res=[0]*len(temperatures)
        for i in range(len(temperatures)-1,-1,-1):
            ele=temperatures[i]
            while st and ele>=temperatures[st[-1]]:
                st.pop()
            if len(st)==0:
                res[i]=0
            else:
                res[i]=st[-1]-i
            st.append(i)
        return res
        