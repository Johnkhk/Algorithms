#TopDown
def numSquares(n):
    memo = {}
    def dfs(factor,cursum):
        if cursum in memo:
            return memo[cursum]
        if cursum==n:
            return 0
        if cursum>n:
            return float("inf")
        if cursum+factor**2>n:
            return float("inf")
    
        # repeat current factor
        a = 1 + dfs(factor, cursum+factor**2)
    
        # add 1 to factor (0cost)
        b = dfs(factor+1,cursum)
    
        memo[cursum] = min(a,b)
        return min(a,b)
    return int(dfs(1,0))

# BottomUp
def numSquares(n):

    square_nums = [i**2 for i in range(0, int(math.sqrt(n))+1)]
    dp = [float('inf')] * (n+1)
    # bottom case
    dp[0] = 0
    
    for i in range(1, n+1):
        for square in square_nums:
            if i < square:
                break
            dp[i] = min(dp[i], dp[i-square] + 1)
    
    return dp[-1]