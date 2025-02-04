
def twoCitySchedCost(costs):


    N = len(costs)
    n = N//2
    anum=bnum=n
    def dfs(i,acount,bcount):
        # case 1: cities uneven, (one city has more than other) 
        if acount>n or bcount>n:
            return float("inf")
        # case 2: both cities have same amount of people and there's no more people
        if acount==n and bcount==n:
            return 0
        # case 3: i out of bounds (This needs to be after case 2_
        if i>=N:
            return float("inf")
        
        # option1 take citya
        opt1 = costs[i][0]+dfs(i+1,acount+1,bcount)
        # option1 take cityb
        opt2 = costs[i][1]+dfs(i+1,acount,bcount+1)
        return min(opt1,opt2)
    ### MISTAKE ###
    # def dfs(i,acount,bcount):
    #     if acount==n and bcount==n:
    #         return 0
    #     if i==N or acount>n or bcount>n:
    #         return float("inf")

    #     # option1 take citya
    #     opt1 = costs[i][0]+dfs(i+1,acount+1,bcount)
    #     # option1 take cityb
    #     opt2 = costs[i][1]+dfs(i+1,acount,bcount+1)
    #     return min(opt1,opt2)
        
    return dfs(0,0,0)

        N = len(costs)
        n = N//2
        anum=bnum=n
        
        return dfs(0,0,0)