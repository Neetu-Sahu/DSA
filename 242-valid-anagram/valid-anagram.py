class Solution(object):
    def isAnagram(self, s, t):
        
        d1={}
        d2={}

        if len(s)!=len(t):
            return False
        else:
            for i in s:
                if i not in d1:
                    d1[i]=1
                else:
                    d1[i]+=1
            for i in t:
                if i not in d2:
                    d2[i]=1
                else:
                    d2[i]+=1
            for i in s:
                if (i in d1 and i not in d2) or d1[i]!=d2[i]:
                    return False
        return True
