class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur=nums[0]
        max_sum=nums[0]
        for i in range(1,len(nums)):
            cur=max(nums[i],cur+nums[i])
            max_sum=max(cur,max_sum)
        return max_sum
             
            
        