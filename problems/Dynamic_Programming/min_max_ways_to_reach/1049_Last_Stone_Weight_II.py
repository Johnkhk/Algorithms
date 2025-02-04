### very similar Problem ###
# 416. Partition Equal Subset Sum
def lastStoneWeightII(stones):
    memo = {}
    def dfs(a,b,arr):
        if (a,b) in memo:
            return memo[(a,b)]
        if len(arr)==0:
            return abs(a-b)
        
        s = arr.pop()
        o1=dfs(a+s,b,arr)
        o2=dfs(a,b+s,arr)
        m = min(o1,o2)
        arr.append(s)
        memo[(a,b)]=m
        return m

    return dfs(0,0,stones)
# 

### JUST A KNAPSACK ###
def lastStoneWeightII(stones):
    
    """
    goal: get the minimum last stone weight from collisions (subsets)
    idea: use dynamic programming
        we fill a knapsack of capacity sum//2 to the max
        we use sum//2 because it works for both odd and even since our answer
        needs to be <= sum//2
        we return total - this max 
    """
    
    total = sum(stones)
    half = total//2
    # dp will hold best weight can hold of capacity index
    dp = [0]*(half+1)
    for stone in stones:
        for i in reversed(range(stone,len(dp))):
            dp[i] = max(dp[i],dp[i-stone]+stone)
    # print(dp)
    return total-2*dp[-1]     