# TopDown
def coinChange(coins, amount):
    memo = {}
    def dfs(curAmount):
        # memo
        if curAmount in memo:
            return memo[curAmount] 
        # base case
        if curAmount==amount:
            return 0
        # base case
        if curAmount > amount:
            return float("inf")
        a = float("inf")
        for j in range(len(coins)):
            a = min(a, 1+dfs(curAmount+coins[j]))
        memo[curAmount] = a
        return a
    res = dfs(0)
    if res==float("inf"):
        return -1
    return dfs(0)
    
#BottomUp
def coinChange(coins, amount):
    # BottomUp
    # We make this amount +1 because because we want basecase 0 to be 0
    dp=[float("inf")]*(amount+1) # then 1 all the way till amount
    dp[0]=0 # base case of 0
    for coin in coins:
        for i in range(coin,amount+1):
            dp[i] = min(dp[i],1+dp[i-coin]) # will be 1 for coins since basecase 0
            
    return dp[-1] if dp[-1]!=float("inf") else -1
