def canPartitionKSubsets(nums, k):
    nums.sort(reverse=True)
    N = len(nums)
    total = sum(nums)
    if total%k!=0:
        return False
    half = int(total/k)
    
    ks=[0]*k
    def dfs(i):
        if i == len(nums):
            for j in ks:
                if j!=half:
                    return False
            return True
        
        for m in range(k):
            if ks[m]+nums[i]<=half:
                ks[m]+=nums[i]
                if dfs(i+1):
                    return True
                ks[m]-=nums[i]
        return False
                
    return dfs(0)

def canPartitionKSubsets(nums, k):
    nums.sort(reverse=True)
    N = len(nums)
    total = sum(nums)
    if total%k!=0:
        return False
    half = int(total/k)
    used=[0]*len(nums)
    def backtracking(i,cursum,partitions):
        
        if cursum==half:
            return backtracking(0,0,partitions)
        if partitions==k-1:
            return True
        # if i >= len(nums):
        #     return False
        
        for j in range(i,len(nums)):
            if not used[j]:
                
                used[j]=1
                
                if cursum<=half:
                    if backtracking(j+1,cursum+nums[j],partitions):
                        return True
                used[j]=0
                
        return False
    
    return backtracking(0,0,0)
            