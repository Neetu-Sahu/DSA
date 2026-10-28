class Solution(object):
    def productExceptSelf(self, nums):
        
        n=len(nums)
        ans=[1]*n

        #Left product
        p=1
        for i in range(n):
            ans[i]=p
            p*=nums[i]

        #Right product*Left product
        p=1
        for i in range(n-1,-1,-1):
            ans[i]*=p
            p*=nums[i]

        return ans
        