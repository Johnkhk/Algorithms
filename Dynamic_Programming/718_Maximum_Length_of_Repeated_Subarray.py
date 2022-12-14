"""
This DP problem is special because the bottom up u have to keep a running res
For topdown cant just return dfs, but do the same. 
just use 2 for loops and running res
"""
# TopDown
def findLength(nums1, nums2):
        
    M,N=len(nums1),len(nums2)
    memo = {}
    def dfs(i,j):
        if (i,j) in memo:
            return memo[(i,j)]
        if i >=len(nums1) or j>=len(nums2):
            return 0
        
        a=0
        if nums1[i]==nums2[j]:
            a = 1+dfs(i+1,j+1)
        
        memo[(i,j)] = a
        return a
    
    res = 0
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] == nums2[j] and res < min(M-i, N-j):
                res = max(res,dfs(i,j))
    return res

# BottomUp
def findLength(nums1, nums2):
    res = float("-inf")
    nums1,nums2 = nums2,nums1
    dp = [[0]*(len(nums2)+1) for i in range(len(nums1)+1)]
    for i in range(1,len(nums1)+1):
        for j in range(1,len(nums2)+1):
            if nums1[i-1]==nums2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = 
                
            res = max(res,dp[i][j])
    return res