class Solution(object):
    def findDisappearedNumbers(self, nums):
        ans=[]
        
        a=set(nums)
        for i in range(1,len(nums)+1):
            if i not in a:
                ans.append(i)

        return ans

        