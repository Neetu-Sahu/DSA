class Solution(object):
    def validPalindrome(self, s):

        n=len(s)
        
        left=0
        right=n-1
        while left<right:
            if s[left]!=s[right]:
                l=left+1
                r=right
                while l<r and s[l]==s[r]:
                    l+=1
                    r-=1
                if l>=r:
                    return True

                l=left
                r=right-1
                while l<r and s[l]==s[r]:
                    l+=1
                    r-=1
                return l>=r

            left+=1
            right-=1

        return True

        