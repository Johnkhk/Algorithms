### Top Down Memoiszation ###
#TC: O(m*n)
#SC: O(m+n) for recursive call, O(m*n) for the memo
def longestCommonSubsequence(text1, text2):
    memo={}
    def dfs(i,j):
        if (i,j) in memo:
            return memo[(i,j)]
        if i==len(text1) or j==len(text2):
            return 0
        
        if text1[i]==text2[j]:
            res = 1 + dfs(i+1,j+1)
        else:
            res = max(dfs(i+1,j),dfs(i,j+1))
        memo[(i,j)]=res
        return res
    return dfs(0,0)

### Bottom Up ###
#TC: O(m*n)
#SC: O(m*n)
def longestCommonSubsequence(text1, text2):
    dp = [[0]*(len(text2)+1) for i in range(len(text1)+1)]
    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            if text1[i-1]==text2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[-1][-1]
