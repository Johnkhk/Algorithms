def minSteps(n):
    if n==1:
        return 0

    memo = {}
    def dfs(clipboard,screen):
        if (clipboard,screen) in memo:
            return memo[(clipboard,screen)]
        if screen>n or clipboard>n:
            return float("inf")
        if screen==n:
            return 0
        
        # copy & paste
        cop = 2+dfs(screen,screen*2)
        
        # paste
        pas = 1+dfs(clipboard,screen+clipboard)
        
        memo[(clipboard,screen)] = min(cop,pas)
        
        return min(cop,pas)
    return 1+dfs(1,1)


# JAVA BottomUp
    # public int minSteps(int n) {
    #     int[] dp = new int[n+1];

    #     for (int i = 2; i <= n; i++) {
    #         dp[i] = i;
    #         for (int j = i-1; j > 1; j--) {
    #             if (i % j == 0) {
    #                 dp[i] = dp[j] + (i/j);
    #                 break;
    #             }
                
    #         }
    #     }
    #     return dp[n];
    # }