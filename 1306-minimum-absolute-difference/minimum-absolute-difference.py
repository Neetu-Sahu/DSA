class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        n=len(arr)
        a=[]
        ans=[]
        
        for i in range(0,n-1):
            a.append(abs(arr[i]-arr[i+1]))
        min_diff=min(a)
        
        for i in range(0,n-1):
            if abs(arr[i]-arr[i+1])==min_diff:
                ans.append([arr[i],arr[i+1]])
        return ans
            
        