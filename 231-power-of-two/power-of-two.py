class Solution(object):
    def isPowerOfTwo(self, n):
        
        count=0

        while n>0:
            if n&1==1:
                count+=1
            n=n>>1
        if count==1:
            return True
        else:
            return False
        