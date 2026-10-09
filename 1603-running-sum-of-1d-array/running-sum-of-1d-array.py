class Solution(object):
    def runningSum(self, nums):
        
        ans=[]

        for i in range(0,len(nums)):
            sum=0
            for j in range(0,i+1):
                sum+=nums[j]
            ans.append(sum)

        return ans
        