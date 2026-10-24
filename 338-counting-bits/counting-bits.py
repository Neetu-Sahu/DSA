class Solution(object):
    def countBits(self, n):

        ans=[]
        
        for i in range(0,n+1):
            count=0
            num=i
            while num>0:
                if num&1==1:
                    count+=1
                num=num>>1
            ans.append(count)

        return ans
        