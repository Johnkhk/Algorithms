class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # m number of 0's
        # n number of 1's
        
        # TopDown
#         c = [Counter(s) for s in strs]
#         memo={}
#         def topdown(i,m,n):
#             if m<0 or n<0:
#                 return float("-inf")
#             if i>=len(strs):
#                 return 0
#             if (i,m,n) in memo:
#                 return memo[(i,m,n)]
            
#             # take
#             opt1 = 1 + topdown(i+1,m-c[i]["0"],n-c[i]["1"])
#             # not take
#             opt2 = topdown(i+1,m,n)
            
#             memo[(i,m,n)] = max(opt1,opt2)
#             return max(opt1,opt2)
            
#         return topdown(0,m,n)
    
        # BottomUp
        c = [Counter(s) for s in strs]
        dp = [[[0]*(n+1) for i in range(m+1)] for j in range(len(strs)+1)]
        # dp = [[0]*(m+1) for j in range(len(strs)+1)]
        
        M,N=m,n
        for i in reversed(range(len(strs))):
        # for i in range(len(strs)):
            for m in reversed(range(M+1)):
                for n in reversed(range(N+1)):
                    opt1=float("-inf")
                    if m-c[i]["0"]>=0 and n-c[i]["1"]>=0:
                        opt1 = 1 + dp[i+1][m-c[i]["0"]][n-c[i]["1"]]
                        # opt1 = 1 + dp[m-c[i]["0"]][n-c[i]["1"]]
                        
                    opt2 = dp[i+1][m][n]
                    # opt2 = dp[m][n]
                    dp[i][m][n] = max(opt1,opt2)
                    # dp[m][n] = max(opt1,opt2)
                    
        # print(dp)
        # return dp[0][M][N]
        return dp[0][M][N]
        
        
        # return dp[M][N]        




class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # m number of 0's
        # n number of 1's
        
        # TopDown
#         c = [Counter(s) for s in strs]
#         memo={}
#         def topdown(i,m,n):
#             if m<0 or n<0:
#                 return float("-inf")
#             if i>=len(strs):
#                 return 0
#             if (i,m,n) in memo:
#                 return memo[(i,m,n)]
            
#             # take
#             opt1 = 1 + topdown(i+1,m-c[i]["0"],n-c[i]["1"])
#             # not take
#             opt2 = topdown(i+1,m,n)
            
#             memo[(i,m,n)] = max(opt1,opt2)
#             return max(opt1,opt2)
            
#         return topdown(0,m,n)
    
        # BottomUp
        c = [Counter(s) for s in strs]
        # dp = [[[0]*(n+1) for i in range(m+1)] for j in range(len(strs)+1)]
        # dp = [[0]*(m+1) for j in range(len(strs)+1)]
        dp = [[0]*(n+1) for j in range(m+1)]
        
        
        M,N=m,n
        # for i in reversed(range(len(strs))):
        for i in range(len(strs)):
            for m in reversed(range(M+1)):
                for n in reversed(range(N+1)):
                    opt1=float("-inf")
                    if m-c[i]["0"]>=0 and n-c[i]["1"]>=0:
                        # opt1 = 1 + dp[i+1][m-c[i]["0"]][n-c[i]["1"]]
                        opt1 = 1 + dp[m-c[i]["0"]][n-c[i]["1"]]
                        
                    # opt2 = dp[i+1][m][n]
                    opt2 = dp[m][n]
                    # dp[i][m][n] = max(opt1,opt2)
                    dp[m][n] = max(opt1,opt2)
                    
        # print(dp)
        # return dp[0][M][N]
        # return dp[0][M][N]
        
        
        return dp[M][N]        



###  fastest optimized
dp = [[0]*(n+1) for j in range(m+1)]
        
        
M,N=m,n
for i in range(len(strs)):
    mc,nc=c[i]["0"],c[i]["1"]
    for m in reversed(range(mc,M+1)):
        for n in reversed(range(nc,N+1)):
            opt1=float("-inf")
            # if m-mci>=0 and n-nci>=0:
                # opt1 = 1 + dp[m-mci][n-nci]
            opt1 = 1 + dp[m-mc][n-nc]
            opt2 = dp[m][n]
            
            dp[m][n] = max(opt1,opt2)
            
            

return dp[M][N]    