
### TopDown ###
# TC: O(2N), SC: O(2N + N) N for the recursice call stack
def maxProfit(prices):
    """
        4 options:
        if u haven't bought:
            -you can buy
            -you can skip
        if u already bought:
            -you can sell
            -you can skip
        So you can make it 3 options
    """
    memo={}
    def dfs(i,bought):
        if (i,bought) in memo:
            return memo[(i,bought)]
        if i>=len(prices):
            return 0
        
        a = b = c = float("-inf")
        # buy
        if bought==False:
            a = dfs(i+1,True) - prices[i] 
        # sell
        if bought==True:
            b = prices[i] + dfs(i+1,False)
        c = dfs(i+1,bought)
        memo[(i,bought)] = max(a,b,c)
        return max(a,b,c)
    return dfs(0,False)

### BottomUp ###
# TC: O(2N), SC: O(2N)
def maxProfit(prices):
    """
    Base case is dp[N]=0. So we need array size of N+1
    Go in reverse cuz bottom up (build from base case)
    literally copy and pasted recurrence relation.
    """
    N=len(prices)
    dp = [[0]*(2) for i in range(N+1)] # N+1 why
    for i in reversed(range(N)):
        for bought in range(2):
            a = b = c = float("-inf")
            # buy
            if bought==False:
                a = dp[i+1][True] - prices[i] 
            # sell
            if bought==True:
                b = prices[i] + dp[i+1][False]
            c = dp[i+1][bought]
            dp[i][bought] = max(a,b,c)
    return dp[0][0]
        
### BottomUp ###
# TC: O(2N), SC: O(4)
def maxProfit(prices):
    """
    Even more space optimized, we only use the previous day
    """
    N=len(prices)
    dp = [[0]*(2) for i in range(2)] # N+1 why
    
    for i in reversed(range(N)):
        for bought in range(2):

            a = b = c = float("-inf")
            # buy
            if bought==False:
                a = dp[1][True] - prices[i] 
            # sell
            if bought==True:
                b = prices[i] + dp[1][False]
            c = dp[1][bought]
            dp[0][bought] = max(a,b,c)
            dp[1]=dp[0]
    return dp[0][0]