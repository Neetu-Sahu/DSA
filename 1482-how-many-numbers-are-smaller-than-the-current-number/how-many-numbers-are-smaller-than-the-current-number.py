class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        
        temp=sorted(nums)

        d={}
        for i,num in enumerate(temp):
            if num not in d:
                d[num]=i
        ans=[]
        for i in nums:
            ans.append(d[i])
        return ans