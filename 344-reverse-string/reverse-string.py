class Solution(object):
    def reverseString(self, s):
        
        beg=0
        end=len(s)-1

        while beg<end:
            s[beg],s[end]=s[end],s[beg]
            beg+=1
            end-=1
        return s
        