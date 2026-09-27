class Solution(object):
    def numIslands(self, grid):

        #using DFS for this problem
        #graph approach is much easier to find out the number of connected components

        row=len(grid)
        col=len(grid[0])
        count=0

        #dfs function
        def dfs(r,c):
            if r<0 or r>=row or c<0 or c>=col or grid[r][c]=="0":
                return
            else:
                grid[r][c]="0"
                dfs(r-1,c)
                dfs(r+1,c)
                dfs(r,c-1)
                dfs(r,c+1)
        for i in range(0,row):
            for j in range(0,col):
                if grid[i][j]=="1":
                    count+=1
                    dfs(i,j)

        return count




    
        