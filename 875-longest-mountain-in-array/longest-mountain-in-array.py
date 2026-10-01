class Solution(object):
    def longestMountain(self, arr):
        
        l=[]
        n=len(arr)
        if len(arr)<3:
            return 0

        for i in range(1,n-1):
            ans=0
            if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                left=i-1
                right=i+1
                ans+=3
                while left>0 and arr[left]>arr[left-1]:
                    ans+=1
                    left-=1
                
                while right<n-1 and arr[right]>arr[right+1]:
                    ans+=1
                    right+=1
            l.append(ans)
        
        return max(l)
            
        