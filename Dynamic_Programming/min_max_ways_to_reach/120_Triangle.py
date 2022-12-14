class Solution:
    def minimumTotal(triangle):
        # TopDown
        memo = {}
        def dfs(r,c):
            if (r,c) in memo:
                return memo[(r,c)]
            if r>=len(triangle):
                return 0
            opt1 = triangle[r][c]+dfs(r+1,c)
            opt2 = triangle[r][c]+dfs(r+1,c+1)            
            memo[(r,c)]=min(opt1,opt2)
            return min(opt1,opt2)
        return dfs(0,0)

class Solution:
    def minimumTotal(triangle):
        # BottomUp
        N = len(triangle)
        dp = [[0]*(N+1) for _ in range(N+1)]
        for r in reversed(range(N)):
            for c in reversed(range(len(triangle[r]))):
                opt1 = triangle[r][c]+dp[r+1][c]
                opt2 = triangle[r][c]+dp[r+1][c+1]          
                dp[r][c] = min(opt1,opt2)
        
        return dp[0][0]

        # BottomUp 1-D
        N = len(triangle)
        dp = triangle[-1]
        for r in reversed(range(N-1)):
            for c in range(len(triangle[r])):
                opt1 = triangle[r][c]+dp[c]
                opt2 = triangle[r][c]+dp[c+1]          
                dp[c] = min(opt1,opt2)

        return dp[0]