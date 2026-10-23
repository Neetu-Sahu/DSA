class Solution(object):
    def reverseWords(self, s):
        
        l=s.split()
        ans=[]

        for i in l:
            a=i[::-1]
            ans.append(a)

        return " ".join(ans)
        