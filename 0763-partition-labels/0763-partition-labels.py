class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d={}
        ans=[]
        for i in range(len(s)):
            d[s[i]]=i
        st=0
        while st<len(s):
            e=d[s[st]]
            fe = d[s[st]]
            i = st
            while i <= e:
                e = max(e, d[s[i]])
                i += 1
            ans.append(e - st + 1)
            st = e + 1
        return ans