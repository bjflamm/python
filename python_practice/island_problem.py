class Solution(object):
    
            
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        
        islandcount = 0
        for row in range(0,len(grid)):
            for col in range(0,len(grid[row])):
                if grid[row][col] == '1':
                    islandcount += 1
                    dfs(grid,row,col)
        return islandcount
    
def dfs(grid,row,col):
            
            if row<0 or row==len(grid) or col < 0 or col == len(grid[row]) or grid[row][col] == '0':
                return grid
            else:
                grid[row][col] = '0'
                dfs(grid,row-1,col)
                dfs(grid,row+1,col)
                dfs(grid,row,col-1)
                dfs(grid,row,col+1)
                return grid    
            
