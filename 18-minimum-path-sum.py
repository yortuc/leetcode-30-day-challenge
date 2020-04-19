#
# Naive solution. Throws 'Time limit exceeded'
#
class Solution:
    
    def __init__(self):
        self.min_cost = float('Inf')
        self.cache = {}
    
    
    def depth_search(self, grid, i, j, cost):
        _cost = cost + grid[i][j]

        kk = f'{i}_{j}'
        if kk not in self.cache:
            self.cache[kk] = _cost
        else:
            if _cost >= self.cache[kk]:
                return
        
        # early terminate
        if _cost >= self.min_cost:
            return
        
        # bottom-right
        if i == len(grid)-1 and j == len(grid[0])-1:
            self.min_cost = min(self.min_cost, _cost)
        
        def go_down():
            if i < len(grid)-1:
                self.depth_search(grid, i+1, j, _cost)
        
        def go_right():
            if j < len(grid[0])-1:
                self.depth_search(grid, i, j+1, _cost)
                
        go_down()
        go_right()

    def minPathSum(self, grid: List[List[int]]) -> int:
        # start from top-left. right or down
        # do a depth first search
        # get the minimum one
        
        self.depth_search(grid, 0, 0, 0)
                
        return self.min_cost


#
# Dynamic programming solution
# https://www.programcreek.com/2014/05/leetcode-minimum-path-sum-java/
#

class Solution:    
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = []
        for p in grid:
            dp.append([None]*n)
        
        dp[0][0] = grid[0][0]
        
        # init top row
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
                    
        # init left col
        for j in range(1, m):
            dp[j][0] = dp[j-1][0] + grid[j][0]
        
        
        # do the dp magic
        #    1  4  5
        #    2  
        #    4 
        
        for i in range(1, m):
            for j in range(1, n):
                right = dp[i-1][j]
                down  = dp[i][j-1]
                
                if down < right:
                    dp[i][j] = grid[i][j] + down
                else:
                    dp[i][j] = grid[i][j] + right
        
        return dp[m-1][n-1]
 
# 61 / 61 test cases passed.
# Status: Accepted
# Runtime: 92 ms
# Memory Usage: 15.4 MB
