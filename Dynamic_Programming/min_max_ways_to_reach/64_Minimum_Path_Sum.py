# TopDown O(m*n) O(m*n)
def minPathSum(self, grid: List[List[int]]) -> int:
    ROWS,COLS = len(grid), len(grid[0])
    memo = {}
    def topdown(r,c):
        if (r,c) in memo:
            return memo[(r,c)]
        if r<0 or c<0 or r>=ROWS or c>=COLS:
            return float("inf")
        if r==ROWS-1 and c==COLS-1:
            return grid[r][c]
        right = grid[r][c] + topdown(r,c+1)
        down = grid[r][c] + topdown(r+1,c)  
        memo[(r,c)] = min(right,down)
        return min(right,down)
    return topdown(0,0)
    
# BottomUp from 0,0
def minPathSum(self, grid: List[List[int]]) -> int:
    ROWS,COLS = len(grid), len(grid[0])
    dp = [[0]*COLS for i in range(ROWS)]
    
    #basecase
    dp[0][0]=grid[0][0]
    for r in range(1,ROWS):
        dp[r][0] = dp[r-1][0] + grid[r][0]
    for c in range(1,COLS):
        dp[0][c] = dp[0][c-1] + grid[0][c]
    
    for r in range(1,ROWS):
        for c in range(1,COLS):
            dp[r][c] = grid[r][c]+min(dp[r-1][c],dp[r][c-1])
    return dp[-1][-1]

# BottomUp from -1,-1
def minPathSum(self, grid: List[List[int]]) -> int:
    ROWS,COLS = len(grid), len(grid[0])
    dp = [[0]*COLS for i in range(ROWS)]
    
    #basecase
    dp[-1][-1]=grid[-1][-1]
    for r in range(ROWS-2,-1,-1):
        dp[r][-1] = dp[r+1][-1] + grid[r][-1]
    for c in range(COLS-2,-1,-1):
        dp[-1][c] = dp[-1][c+1] + grid[-1][c]
    print(dp)
    for r in range(ROWS-2,-1,-1):
        for c in range(COLS-2,-1,-1):
            dp[r][c] = grid[r][c]+min(dp[r+1][c],dp[r][c+1])
    return dp[0][0]

        
    
    
            