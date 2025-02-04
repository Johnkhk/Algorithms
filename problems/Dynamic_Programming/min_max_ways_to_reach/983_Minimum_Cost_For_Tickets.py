# TopDown 1, 
def mincostTickets(days, costs):
    memo = {} # Not even a 2d Memo
    def dfs(i,day):
        if i==len(days):
            return 0
        if day>days[i]: # This here is special, we use this to keep iterating above
            return dfs(i+1,day)
        if i in memo:
            return memo[i]
        
        # buy 1-day
        a = costs[0] + dfs(i+1, days[i]+1)
        
        # buy 7-day            
        b = costs[1] + dfs(i+1, days[i]+7)
        
        # buy 30-day            
        c = costs[2] + dfs(i+1, days[i]+30)
        
        memo[i] = min(a,b,c)
        return min(a,b,c)
    return dfs(0,0)

# The other way to do this is to interatie inside until we above.
def mincostTickets(days, costs):
    memo = {} # Not even a 2d Memo
    def dfs(i):
        if i>=len(days):
            return 0
        if i in memo:
            return memo[i]
        
        # buy 1-day
        j=i+1
        while j<len(days) and days[j] < 1+days[i]:
            j+=1
        a = costs[0] + dfs(j)
        
        # buy 7-day  
        j=i+1
        while j<len(days) and days[j] < 7+days[i]:
            j+=1
        b = costs[1] + dfs(j)
        
        # buy 30-day            
        j=i+1
        while j<len(days) and days[j] < 30+days[i]:
            j+=1
        c = costs[2] + dfs(j)
        
        memo[i] = min(a,b,c)
        return min(a,b,c)
    return dfs(0)

# BottomUp
def mincostTickets(days, costs):
    dp = [0]*(days[-1]+1) # base case is 0th day cost 0
    days=set(days)
    for i in range(1,len(dp)):
        if i in days:
            d1 = dp[max(0,i-1)]+costs[0] # the max is so if we out of bounds use most recent day
            d2 = dp[max(0,i-7)]+costs[1]
            d3 = dp[max(0,i-30)]+costs[2]
            
            dp[i] = min(d1,d2,d3)
        else:
            dp[i]=dp[i-1] # also for 0th case
    return dp[-1]