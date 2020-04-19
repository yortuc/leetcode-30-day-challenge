class Solution:        
    def __init__(self):
        self.count = 0
    
    
    def process_cell(self, cache, grid, i, j):
        def get(x, y):
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1':
                return (x, y)
            else:
                return None

        if (i,j) in cache or grid[i][j] == '0':
            return
        
        self.count += 1
        stack = [(i, j)]
        
        while stack:
            
            cur = stack.pop()
            
            if cur in cache:
                continue
            
            cache.add(cur)
            
            # get neighbors
            ci, cj = cur[0], cur[1]

            neighbors = [                get(ci, cj-1),      
                          get(ci-1, cj),                 get(ci+1, cj),
                                         get(ci, cj+1)
                        ]
            neighbors = [t for t in neighbors if t]

            for n in neighbors:
                if n not in cache:
                    stack.append(n)
                    
                        
    def numIslands(self, grid: List[List[str]]) -> int:
        # iterate over grid
        # process each cell if it's 1, save to a cache (set)
        #   process of a cell:
        #      breadth first search
        #      untill all neighbors are 0
        #
                        
        cache = set()
    
        for i in range(len(grid)):            
            for j in range(len(grid[i])):
                self.process_cell(cache, grid, i, j)
        
        return self.count
        

# 47 / 47 test cases passed.
# Status: Accepted
# Runtime: 184 ms
# Memory Usage: 18.8 MB

