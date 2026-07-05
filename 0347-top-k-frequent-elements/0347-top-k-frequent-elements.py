class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        ds=dict(sorted(d.items(),key=lambda x:x[1]))
        l=list(ds.keys())
        c=0
        ans=[]
        for i in range(len(l)-1,-1,-1):
            ans.append(l[i])
            c+=1
            if c==k:
                break
        return ans
