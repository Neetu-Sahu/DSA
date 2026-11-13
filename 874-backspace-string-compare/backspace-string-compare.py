class Solution(object):
    
    def backspaceCompare(self, s, t):
        s2 = ""
        t2 = ""
        
        for char in s:
            if char == "#":
                s2 = s2[:-1]
            else:
                s2 += char
                
        for char in t:
            if char == "#":
                t2 = t2[:-1]
            else:
                t2 += char

        return t2 == s2
