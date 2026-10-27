class Solution(object):
    def majorityElement(self, nums):
        
        n=len(nums)

        d={}

        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1

        for i in d:
            if d[i]>n//2:
                return i
        