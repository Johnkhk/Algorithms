# TopDown
def minFallingPathSum(matrix):
    R,C = len(matrix),len(matrix[0])
    memo={}
    def dfs(r,c):
        if (r,c) in memo:
            return memo[(r,c)]
        if c>=C or c<0:
            return float("inf")
        if r>=R:
            return 0
        d  = dfs(r+1,c)
        dl = dfs(r+1,c-1)
        dr = dfs(r+1,c+1) 
        
        memo[(r,c)] = min(d,dl,dr) + matrix[r][c]
        return min(d,dl,dr) + matrix[r][c]
    
    a = float("inf")
    for i in range(C):
        a = min(a,dfs(0,i))
    return a

# BottomUp
def minFallingPathSum(matrix):
    R,C = len(matrix),len(matrix[0])
    dp = [[float("inf")]*(C+2) for i in range(R+1)]
    dp[0] =[0]*(C+2)
    # print(dp)
    for r in range(1,R+1):
        for c in range(1,C+1):
            dp[r][c] = matrix[r-1][c-1]+min(dp[r-1][c-1],dp[r-1][c],dp[r-1][c+1])
    return min(dp[-1])

# BottomUp Clean
def minFallingPathSum(matrix):
    R,C = len(matrix),len(matrix[0])
    dp = [[float("inf")]*C for i in range(R)]
    dp[0] = matrix[0]
    # print(dp)
    for r in range(1,R):
        for c in range(C):
            dp[r][c] = matrix[r][c]+min(dp[r-1][max(0,c-1)],dp[r-1][c],dp[r-1][min(c+1,C-1)])
    return min(dp[-1])