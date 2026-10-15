class Solution(object):
    def getSum(self, a, b):

        mask=0xFFFFFFFF
        
        while b!=0:
            carry=(a&b)<<1
            a=(a^b) & mask
            b=carry & mask

        if a>=0x80000000:
            a=~(a^mask)

        return a
        