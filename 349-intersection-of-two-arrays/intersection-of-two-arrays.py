class Solution(object):
    def intersection(self, nums1, nums2):
        
        ans=[]

        for i in nums1:
            if i not in ans and i in nums2: 
                ans.append(i)

        return ans
        