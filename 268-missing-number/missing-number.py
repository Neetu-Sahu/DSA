class Solution(object):

    #O(nlog n) complexity
    def missingNumber(self, nums):
    #   
    #  nums.sort()
    # for a,b in enumerate(nums):
    #    if a!=b:
    #       return a
    #if len(nums) not in nums:
    #   return len(nums)

    #O(n) time complexity
         return sum(range(len(nums)+1))-sum(nums)


        
        