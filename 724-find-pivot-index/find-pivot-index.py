class Solution(object):
    def pivotIndex(self, nums):
        
        leftsum=0
        totalsum=sum(nums)

        for i in range(len(nums)):
            rightsum=totalsum-nums[i]-leftsum

            if rightsum==leftsum:
                return i
            leftsum+=nums[i]

        return -1        