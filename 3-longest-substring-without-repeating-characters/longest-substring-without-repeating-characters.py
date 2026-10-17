class Solution(object):
    def lengthOfLongestSubstring(self, s):

        store=set()
        maxi=0
        left=0

        for right in range(len(s)):
            while s[right] in store:
                store.remove(s[left])
                left+=1
            store.add(s[right])
            length=right-left+1
            maxi=max(length,maxi)
        
        return maxi
        