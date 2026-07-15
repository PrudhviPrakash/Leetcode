class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st=[]
        d={}
        for i in range(len(nums2)-1,-1,-1):
            ele=nums2[i]
            while st and ele>st[-1]:
                st.pop()
            if len(st)==0:
                d[ele]=-1
            else:
                d[ele]=st[-1]
            st.append(ele)
        res=[]
        for i in nums1:
            res.append(d[i])
        return res