def minCostClimbingStairs(cost):
    # TopDown
    memo = {}
    def dfs(i):
        if i in memo:
            return memo[i]
        if i >=len(cost):
            return 0
        a=dfs(i+2)
        b=dfs(i+1)
        memo[i] = min(a,b) + cost[i]
        return min(a,b) + cost[i]

def minCostClimbingStairs(cost):
    # BottomUp O(n)
    dp = [0]*(len(cost)+1)
    for i in range(2,len(cost)+1):
        dp[i] = min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
    return dp[-1]

def minCostClimbingStairs(cost):
    # BottomUp O(n), O(1) space
    dp = [0]*3
    for i in range(2,len(cost)+1):
        # dp[i] = min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        dp[2] = min(dp[1]+cost[i-1],dp[0]+cost[i-2])
        dp[0],dp[1] = dp[1],dp[2]
    return dp[2]