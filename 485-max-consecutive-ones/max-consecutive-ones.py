class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        
        maxcount=0
        count=0
        if len(nums)==1 and nums[0]==1:
            return 1
        if len(nums)==1 and nums[0]==0:
            return 0

        for i in range(len(nums)-1):
            if nums[i]==0 and nums[i+1]==1 and i+1==len(nums)-1:
                count+=1
                maxcount=max(count,maxcount)
            elif nums[i]==1 and nums[i+1]==0:
                count+=1
                maxcount=max(count,maxcount)
                count=0
            elif nums[i]==0:
                continue
            elif nums[i+1]==1 and i+1==len(nums)-1:
                count+=2
                maxcount=max(count,maxcount)
            else:
                count+=1

        return maxcount

            
        