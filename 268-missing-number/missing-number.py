class Solution(object):
    def missingNumber(self, nums):
        
        nums.sort()
        for a,b in enumerate(nums):
            if a!=b:
                return a
        if len(nums) not in nums:
            return len(nums)
        
        