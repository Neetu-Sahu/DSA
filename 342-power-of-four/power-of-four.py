class Solution(object):
    def isPowerOfFour(self, n):
        
        count=0
        position=0

        while n>0:
            if n&1==1:
                count+=1
                if position%2!=0:
                    return False

            position+=1
            n=n>>1
        if count==1:
            return True
        else:
            return False
        
        