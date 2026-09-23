class Solution(object):
    def twoSum(self, nums, target):
        
        d={}
        for i,num in enumerate(nums):
            s=target-num
            if s in d:
                return [d[s],i]
            else:
                d[num]=i

        