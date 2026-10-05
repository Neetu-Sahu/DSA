class Solution(object):
    def minSubArrayLen(self, target, nums):
        
        ans=len(nums)+1
        left=0
        total=0

        for right in range(len(nums)):
            total+=nums[right]
            
            while total>=target:
                ans=min(ans,right-left+1)
                total-=nums[left]
                left+=1
        if ans==len(nums)+1:
            return 0
        return ans
        