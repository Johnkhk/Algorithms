# TopDown
def canPartition(nums):
    if sum(nums)%2==1:
        return False
    @cache
    def dfs(i,cur):
        if i >=len(nums) or cur<0:
            return False
        if cur==0:
            return True
        
        return dfs(i+1,cur) or dfs(i+1, cur-nums[i])
    
    return dfs(0,int(sum(nums)/2))

# BottomUp   
def canPartition(nums):
    Total = sum(nums)
    if Total%2==1:
        return False
    half = int(Total/2)
    dp = [True]+[False]*half
    
    for num in nums:
        ### THE REASON WE NEED TO REVERSE ###
        # Often times for single dim DP, atleast here, our base case is at the left, and we have dp[i-num], 
        # which is values from previous row if this was 2D. Since it is of dp[i-num], we never need anything from dp[i>],
        # Therefore we go right to left to not overwrite answers. 
        for i in reversed(range(num, half+1)):
        # for i in reversed(range(half+1)):
            # if i-num<0:
                # continue
            dp[i] = dp[i] or dp[i-num]
    
    return dp[-1]

# Bitmask BottomUp
def canPartition(nums):
    N = len(nums)
    total = sum(nums)
    if total&1:
        return False
    half = int(total/2)

    dp = 1 # 1 means true, so we are saying the first base case is true 0th idx
    for num in nums:
        dp = dp | dp<<num 
        # dp|=dp<<num
    return dp & 1 << half # CHECK IF THE bit at half is set